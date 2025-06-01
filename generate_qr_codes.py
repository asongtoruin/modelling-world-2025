from decimal import Decimal
from pathlib import Path

import qrcode
from qrcode.compat.etree import ET
from qrcode.image.svg import SvgPathFillImage
from qrcode.image.styles.moduledrawers.svg import SvgPathCircleDrawer


# Force white-coloured QR codes
SvgPathFillImage.QR_PATH_STYLE["fill"] = "white"
SvgPathFillImage.background = "rgba(255, 255, 255, 0)"

links = {
    "this_presentation": "https://asongtoruin.github.io/modelling-world-2025/",
    "land-use": "https://github.com/Transport-for-the-North/Land-Use",
    "land-use-docs": "https://tfn-land-use-test.readthedocs.io"
}

qrcodes_folder = Path("_static/qr_codes")
qrcodes_folder.mkdir(exist_ok=True)

for desc, link in links.items():

    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=2)
    qr.add_data(link)

    img = qr.make_image(
        image_factory=SvgPathFillImage,
        module_drawer=SvgPathCircleDrawer(size_ratio=Decimal(0.75)),
    )

    # Library doesn't seem to let us do a dimension-less SVG. Get the XML instead
    svg = img._img

    # Pop the height and width attrs
    svg.attrib.pop("height")
    svg.attrib.pop("width")

    # Make it clickable! We need to wrap all children (which may include a separate background) in the a
    link = ET.Element("a", attrib={"href": link, "target": "_blank"})
    elements = [x for x in svg]
    for i, elem in enumerate(elements):
        svg.remove(elem)
        link.insert(i, elem)

    svg.insert(0, link)

    # Rather than img.to_string, we have to use the ET implementation
    with (qrcodes_folder / f"{desc}.svg").open("w") as output_file:
        output_file.write(ET.tostring(svg, encoding="unicode"))
