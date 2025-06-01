from decimal import Decimal
from pathlib import Path

import qrcode
from qrcode.compat.etree import ET
from qrcode.image.svg import SvgPathImage
from qrcode.image.styles.moduledrawers.svg import SvgPathCircleDrawer


# Force white-coloured QR codes
SvgPathImage.QR_PATH_STYLE["fill"] = "#ffffff"

links = {
    "this_presentation": "https://asongtoruin.github.io/modelling-world-2025/",
    "land-use": "https://github.com/Transport-for-the-North/Land-Use",
    "land-use-docs": "https://tfn-land-use-test.readthedocs.io"
}

qrcodes_folder = Path("_static/qr_codes")
qrcodes_folder.mkdir(exist_ok=True)

for desc, link in links.items():

    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(link)

    img = qr.make_image(
        image_factory=SvgPathImage,
        module_drawer=SvgPathCircleDrawer(size_ratio=Decimal(0.75)),
    )

    # Library doesn't seem to let us do a dimension-less SVG. Get the XML instead
    svg = img._img

    # Pop the height and width attrs
    svg.attrib.pop("height")
    svg.attrib.pop("width")

    # Make it clickable!
    link = ET.Element("a", attrib={"href": link, "target": "_blank"})
    path = svg.find("path")
    link.insert(0, path)
    svg.remove(path)
    svg.insert(0, link)

    # Rather than img.to_string, we have to use the ET implementation
    with (qrcodes_folder / f"{desc}.svg").open("w") as output_file:
        output_file.write(ET.tostring(svg, encoding="unicode"))
