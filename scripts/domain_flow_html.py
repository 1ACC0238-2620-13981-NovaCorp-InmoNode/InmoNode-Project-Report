"""Standalone HTML walkthroughs for the report's existing message definitions."""
import json
from html import escape
from pathlib import Path

TEMPLATES = Path(__file__).parent / "templates"
ROUTES = {
    "1B": [
        ("correcta", "Lectura correcta", ["1", "2", "3", "4"], "La imagen es legible y los datos extraídos son correctos. La evidencia queda lista para sincronizar."),
        ("correccion", "Corrección manual", ["1", "2", "3", "4", "5", "6"], "Se corrige una lectura incorrecta o incompleta antes de sincronizar la evidencia."),
        ("recaptura", "Imagen ilegible: recaptura", ["1", "2", "1"], "La primera imagen es ilegible. Se solicita una nueva captura y luego se vuelve a evaluar su legibilidad."),
    ],
    "1C": [
        ("aceptada", "Reserva consolidada", ["1", "2A", "3", "4", "5"], "La reserva se consolida; después se sincroniza su evidencia para revisión financiera."),
        ("conflicto", "Conflicto de disponibilidad", ["1", "2B"], "La reserva queda en conflicto. Se conserva el prospecto y los vouchers permanecen visibles en el dispositivo."),
    ],
    "2B": [
        ("aceptada", "Bloqueo confirmado", ["1", "2", "3A", "4A", "5A"], "La autoridad central confirma el bloqueo antes de habilitar la asociación del comprobante."),
        ("rechazada", "Bloqueo rechazado", ["1", "2", "3B", "4B"], "El lote ya está tomado. Se informa el rechazo sin publicar Solicitud de separación registrada."),
    ],
    "2F": [
        ("expirada", "Reserva expirada", ["1", "2", "5", "6A"], "Venció el plazo más el margen de entrega, sin evidencia retenida. El lote se libera."),
        ("restablecida", "Restablecimiento por entrega tardía", ["1", "2", "3", "4", "5", "6B"], "La evidencia se recibió a tiempo, pero se entregó con retraso. Se restablece la reserva si el lote sigue disponible."),
    ],
    "3": [
        ("primero", "Primer lote del proyecto", [str(i) for i in range(1, 10)], "La publicación del primer lote también activa el proyecto."),
        ("posterior", "Lote de un proyecto ya activo", [str(i) for i in range(1, 10) if i != 8], "Se incorpora un lote adicional. No se vuelve a emitir Proyecto activado."),
    ],
}


def routes_for(item):
    routes = ROUTES.get(item["code"], [("principal", "Recorrido principal", [m["step"] for m in item["messages"]], item["note"])])
    known = {m["step"] for m in item["messages"]}
    assert all(steps and set(steps) <= known for _, _, steps, _ in routes)
    assert set().union(*(set(steps) for _, _, steps, _ in routes)) == known
    return [dict(id=key, label=label, steps=steps, description=description) for key, label, steps, description in routes]


def html_outputs(flows, groups):
    css = (TEMPLATES / "domain-flow.css").read_text(encoding="utf-8")
    js = (TEMPLATES / "domain-flow.js").read_text(encoding="utf-8")
    template = (TEMPLATES / "domain-flow.html").read_text(encoding="utf-8")
    outputs = {}
    options = lambda selected: "".join(f'<option value="flow-{f["code"]}.html"{" selected" if f["code"] == selected else ""}>{escape(f["code"] + " · " + f["title"])}</option>' for f in flows)
    for flow in flows:
        payload = dict(flow, routes=routes_for(flow))
        data = json.dumps(payload, ensure_ascii=False).replace("<", "\\u003c")
        fallback = "".join(f'<li><h3>{escape(flow["code"] + "." + m["step"] + " · " + m["name"])}</h3><p>{escape(m["kind"] + ": " + m["sender"] + " → " + m["receiver"])}</p><p>{escape(m["data"])}</p><p>{escape(m["condition"])}</p></li>' for m in flow["messages"])
        page = template
        for token, value in {
            "__CSS__": css, "__JS__": js, "__DATA__": data,
            "__TITLE__": escape(flow["title"]), "__CODE__": escape(flow["code"]),
            "__NOTE__": escape(flow["note"]), "__OPTIONS__": options(flow["code"]),
            "__FALLBACK__": fallback,
        }.items():
            page = page.replace(token, value)
        outputs[f'flow-{flow["code"]}.html'] = page.encode("utf-8")
    by_code = {f["code"]: f for f in flows}
    sections = []
    for group in groups:
        links = []
        for code in group["codes"]:
            item = by_code[code]
            routes = routes_for(item)
            route_label = f'{len(routes)} rutas' if len(routes) > 1 else 'Recorrido principal'
            links.append(f'<li><a class="directory-link" href="flow-{code}.html"><span class="flow-code">{code}</span><span>{escape(item["title"])}</span><small>{route_label}</small><span aria-hidden="true">&rarr;</span></a></li>')
        sections.append(f'<section><h2>{escape(group["title"])}</h2><ul class="directory-list">{"".join(links)}</ul></section>')
    outputs["index.html"] = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Flujos paso a paso · inmoNode</title><style>{css}</style></head>
<body><a class="skip-link" href="#contenido">Ir al contenido</a><header class="topbar"><a class="brand" href="index.html">inmoNode<span> / Flujos de dominio</span></a><a href="../../../docs/Chapter-02.md#2512-domain-message-flows-modeling">Ver informe</a></header>
<main class="directory" id="contenido"><h1>Un mensaje a la vez.</h1><p class="lead">Recorre los flujos de inmoNode paso a paso. Sigue quién envía cada mensaje, quién lo recibe y qué condiciones permiten continuar.</p><p>Elige un subflujo. Cuando existan alternativas, podrás seleccionar la ruta que quieres revisar.</p>{"".join(sections)}</main><footer class="site-footer">Domain Message Flows Modeling · Capítulo II · inmoNode</footer></body></html>'''.encode("utf-8")
    return outputs
