import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from PIL import Image

def create_cv():
    pdf_path = "/home/smsitutul/Desktop/yeasin/Yeasin_Bhuiyan_CV.pdf"
    width, height = A4 # 595.27 x 841.89
    c = canvas.Canvas(pdf_path, pagesize=A4)
    c.setTitle("Yeasin Bhuiyan - Curriculum Vitae")
    c.setAuthor("Yeasin Bhuiyan")
    c.setSubject("Curriculum Vitae of Yeasin Bhuiyan, EEE Student at JSTU")

    # Colors
    SIDEBAR_BG = colors.HexColor("#123743")
    SIDEBAR_DARK = colors.HexColor("#0d2932")
    AMBER = colors.HexColor("#e5a024")
    SIDEBAR_TEXT = colors.HexColor("#f1f5f9")
    SIDEBAR_MUTED = colors.HexColor("#94a3b8")
    TEXT_DARK = colors.HexColor("#0f172a")
    TEXT_MUTED = colors.HexColor("#334155")
    LINE_COLOR = colors.HexColor("#cbd5e1")
    PRIMARY_BLUE = colors.HexColor("#0284c7")

    sidebar_w = 205

    # 1. Left Sidebar Background
    c.setFillColor(SIDEBAR_BG)
    c.rect(0, 0, sidebar_w, height, fill=1, stroke=0)

    # 2. Sidebar Profile Image
    img_path = "/home/smsitutul/Desktop/yeasin/profile.png"
    photo_h = 210
    photo_y = height - photo_h

    if os.path.exists(img_path):
        c.saveState()
        # Create angled polygon clipping path
        p = c.beginPath()
        p.moveTo(0, height)
        p.lineTo(sidebar_w, height)
        p.lineTo(sidebar_w, photo_y + 25)
        p.lineTo(0, photo_y - 10)
        p.close()
        c.clipPath(p, stroke=0)

        # Draw zoomed profile image to eliminate paper borders
        img_x = -25
        img_y = photo_y - 25
        img_w = sidebar_w + 50
        img_h = photo_h + 55
        c.drawImage(img_path, img_x, img_y, width=img_w, height=img_h, preserveAspectRatio=True, mask='auto')
        c.restoreState()

        # Accent diagonal decorative slashes
        c.setFillColor(SIDEBAR_DARK)
        poly = c.beginPath()
        poly.moveTo(0, photo_y - 10)
        poly.lineTo(sidebar_w, photo_y + 25)
        poly.lineTo(sidebar_w, photo_y + 17)
        poly.lineTo(0, photo_y - 18)
        poly.close()
        c.drawPath(poly, fill=1, stroke=0)

        c.setFillColor(AMBER)
        poly2 = c.beginPath()
        poly2.moveTo(0, photo_y - 18)
        poly2.lineTo(sidebar_w, photo_y + 17)
        poly2.lineTo(sidebar_w, photo_y + 14)
        poly2.lineTo(0, photo_y - 21)
        poly2.close()
        c.drawPath(poly2, fill=1, stroke=0)

    # Sidebar Content starting Y
    sy = photo_y - 36

    # Helper function for sidebar headings
    def draw_sidebar_heading(title):
        nonlocal sy
        # Small amber icon shape
        c.setFillColor(AMBER)
        c.circle(18, sy + 3.5, 3.5, fill=1, stroke=0)
        c.setFillColor(SIDEBAR_BG)
        c.circle(18, sy + 3.5, 1.5, fill=1, stroke=0)

        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(28, sy, title.upper())
        sy -= 14

    # Sidebar Paragraph style
    def sidebar_p(text, size=8, color=SIDEBAR_TEXT, bold=False, leading=10.5):
        nonlocal sy
        style = ParagraphStyle(
            name='SideP',
            fontName='Helvetica-Bold' if bold else 'Helvetica',
            fontSize=size,
            leading=leading,
            textColor=color
        )
        p = Paragraph(text, style)
        w, h = p.wrap(sidebar_w - 28, 200)
        p.drawOn(c, 15, sy - h)
        sy -= (h + 2.5)

    # --- CONTACT ---
    draw_sidebar_heading("Contact")
    sidebar_p("yeasinbhuiyan265@gmail.com", size=7.8, color=SIDEBAR_TEXT)
    sidebar_p("+880 1575 151636", size=7.8, color=SIDEBAR_TEXT)
    sidebar_p("JSTU, Jamalpur, Bangladesh", size=7.8, color=SIDEBAR_MUTED)
    sidebar_p("github.com/smshaiful", size=7.8, color=SIDEBAR_TEXT)
    sy -= 8

    # --- EDUCATION ---
    draw_sidebar_heading("Education")
    sidebar_p("B.Sc. in Electrical & Electronic Eng.", size=8, bold=True, color=colors.white)
    sidebar_p("<i>Jamalpur Sci. & Tech. Univ. (JSTU)</i>", size=7.5, color=SIDEBAR_MUTED)
    sidebar_p("Ongoing Undergraduate Program", size=7, color=AMBER)
    sy -= 4

    sidebar_p("Higher Secondary Certificate (HSC)", size=8, bold=True, color=colors.white)
    sidebar_p("<i>Birshrestha Noor Mohammad Public College</i>", size=7.5, color=SIDEBAR_MUTED)
    sidebar_p("Completed: 2022 | Dhaka Board | <b>GPA 5.00</b>", size=7, color=SIDEBAR_TEXT)
    sy -= 4

    sidebar_p("Secondary School Certificate (SSC)", size=8, bold=True, color=colors.white)
    sidebar_p("<i>Ragdail I.M. High School</i>", size=7.5, color=SIDEBAR_MUTED)
    sidebar_p("Completed: 2020 | Cumilla Board | <b>GPA 5.00</b>", size=7, color=SIDEBAR_TEXT)
    sy -= 8

    # --- SKILLS ---
    draw_sidebar_heading("Technical Skills")
    skills = [
        "Circuit Design & Hardware Prototyping",
        "Digital Electronics & Logic Systems",
        "OrCAD / PSpice Circuit Simulation",
        "MATLAB & Simulink Modeling",
        "Python & C Programming",
        "Arduino Microcontrollers (Nano, Uno)",
        "Biomedical Instrumentation (ECG, AD8232)",
        "Sensor Interfacing & Telemetry",
        "Motor Drivers & Actuation (L298N)",
        "Tinkercad IoT Simulation"
    ]
    for sk in skills:
        c.setFillColor(AMBER)
        c.circle(18, sy - 3.5, 2, fill=1, stroke=0)
        c.setFillColor(SIDEBAR_TEXT)
        c.setFont("Helvetica", 7.8)
        c.drawString(26, sy - 6.5, sk)
        sy -= 11.5
    sy -= 6

    # --- AWARDS & ACTIVITIES ---
    draw_sidebar_heading("Projects & Honors")
    sidebar_p("<b>ROBOFUSION 1.0 (Clever Sapiens)</b>", size=7.8, color=colors.white)
    sidebar_p("Real-Time ECG Monitor Demonstration", size=7, color=SIDEBAR_MUTED)
    sy -= 3
    sidebar_p("<b>Fire Fighting Robot Automation</b>", size=7.8, color=colors.white)
    sidebar_p("Autonomous Sensor-Guided Suppression", size=7, color=SIDEBAR_MUTED)
    sy -= 3
    sidebar_p("<b>Smart Home IoT Simulation</b>", size=7.8, color=colors.white)
    sidebar_p("Sensor & Relay Architecture in Tinkercad", size=7, color=SIDEBAR_MUTED)

    # ================= RIGHT CONTENT =================
    rx = sidebar_w + 24
    rw = width - rx - 24
    ry = height - 44

    # Name Header
    c.setFillColor(TEXT_DARK)
    c.setFont("Helvetica-Bold", 27)
    c.drawString(rx, ry, "Yeasin Bhuiyan")
    ry -= 18

    # Subtitle
    c.setFillColor(PRIMARY_BLUE)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(rx, ry, "EEE Researcher & Embedded Systems Engineer")
    ry -= 22

    # Section Helper
    def right_heading(title):
        nonlocal ry
        c.setFillColor(TEXT_DARK)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(rx, ry, title)
        ry -= 6
        c.setStrokeColor(PRIMARY_BLUE)
        c.setLineWidth(1.5)
        c.line(rx, ry, rx + 38, ry)
        ry -= 12

    # Profile Section
    right_heading("Profile")
    profile_text = (
        "Dedicated Electrical and Electronic Engineering (EEE) student at Jamalpur Science and Technology "
        "University (JSTU) specializing in practical circuit design, microcontroller systems, biomedical "
        "instrumentation, and autonomous hardware. Experienced in engineering real-time biopotential acquisition "
        "stations (ECG), developing high-speed multithreaded Python telemetry GUIs, designing autonomous "
        "fire-fighting robotics, and architecting IoT sensor simulations. Passionate about analog-to-digital "
        "interfacing and building reliable, real-world hardware prototypes."
    )
    style_profile = ParagraphStyle(
        name='Profile',
        fontName='Helvetica',
        fontSize=8.3,
        leading=12,
        textColor=TEXT_MUTED,
        alignment=TA_LEFT
    )
    p_prof = Paragraph(profile_text, style_profile)
    pw, ph = p_prof.wrap(rw, 200)
    p_prof.drawOn(c, rx, ry - ph)
    ry -= (ph + 18)

    # Work / Project Experience Section
    right_heading("Project & Engineering Experience")

    projects = [
        {
            "role": "Lead Hardware & Signal Developer — DIY ECG Machine",
            "meta": "2024 — Present | Jamalpur Science & Technology University",
            "bullets": [
                "Engineered a real-time Electrocardiogram (ECG) monitor integrating AD8232 biopotential analog front-end and Arduino Nano with serial synchronization.",
                "Designed multi-stage active analog filtration and instrumentation amplification to suppress 50Hz AC mains noise and baseline wander.",
                "Built a 60fps multithreaded Python GUI (Robofusion 1.0) with real-time waveform plotting and R-wave BPM calculation.",
                "Repository: github.com/smshaiful/Project-ECG-Machine-Arduino-Nano | Demo: youtu.be/joZa_iyXXQM"
            ]
        },
        {
            "role": "Autonomous Robotics Developer — Fire Fighting Robot",
            "meta": "2024 | Academic Hardware & Robotics Labs, JSTU",
            "bullets": [
                "Developed an autonomous emergency response robot equipped with a 3-channel flame sensor array and L298N dual H-bridge motor driver.",
                "Implemented intelligent flame tracking algorithms and automated water pump servo targeting for rapid fire extinguishing.",
                "Demonstrated reliable fire suppression performance in physical test scenarios. Video Demo: facebook.com/share/v/1BFJxyfnTD/"
            ]
        },
        {
            "role": "Simulation & IoT Designer — Smart Home Automation",
            "meta": "2023 — 2024 | Autodesk Tinkercad Simulation & Prototyping",
            "bullets": [
                "Architected and simulated a multi-sensor smart-home control system in Tinkercad utilizing an Arduino Uno controller.",
                "Interfaced PIR motion detection for automated lighting, ultrasonic sensors for security monitoring, and gas leakage alert with buzzer actuation.",
                "Simulated relay-driven AC appliance control, optimizing power efficiency and component protection."
            ]
        }
    ]

    # Calculate exact timeline positions
    timeline_x = rx + 4.5
    node_y_list = []

    # Dry run to know positions of each node
    temp_ry = ry
    style_role = ParagraphStyle('Role', fontName='Helvetica-Bold', fontSize=9.2, leading=11.5, textColor=TEXT_DARK)
    style_meta = ParagraphStyle('Meta', fontName='Helvetica', fontSize=7.8, leading=10, textColor=PRIMARY_BLUE)
    style_bullet = ParagraphStyle('Bullet', fontName='Helvetica', fontSize=7.8, leading=10.8, textColor=TEXT_MUTED)

    content_x = rx + 16
    content_w = rw - 16

    rendered_items = []
    for proj in projects:
        node_y = ry - 2.5
        node_y_list.append(node_y)

        p_meta = Paragraph(proj["meta"], style_meta)
        mw, mh = p_meta.wrap(content_w, 50)

        p_role = Paragraph(proj["role"], style_role)
        rw_r, rh_r = p_role.wrap(content_w, 50)

        rendered_bullets = []
        for b in proj["bullets"]:
            b_text = f"• {b}"
            p_b = Paragraph(b_text, style_bullet)
            bw, bh = p_b.wrap(content_w, 100)
            rendered_bullets.append((p_b, bh))

        rendered_items.append((node_y, p_meta, mh, p_role, rh_r, rendered_bullets))

        # Advance ry
        ry -= (mh + rh_r + 4)
        for _, bh in rendered_bullets:
            ry -= (bh + 2)
        ry -= 8

    # Draw continuous timeline vertical line from first node to last node
    if len(node_y_list) >= 2:
        c.setStrokeColor(LINE_COLOR)
        c.setLineWidth(1)
        c.line(timeline_x, node_y_list[0], timeline_x, node_y_list[-1])

    # Now draw items and node circles
    curr_y = height - 44 - 18 - 22 - (ph + 18 + 18) - 18
    for node_y, p_meta, mh, p_role, rh_r, bullets in rendered_items:
        # Timeline node circle
        c.setFillColor(colors.white)
        c.setStrokeColor(PRIMARY_BLUE)
        c.setLineWidth(1.5)
        c.circle(timeline_x, node_y, 3.5, fill=1, stroke=1)

        # Meta
        p_meta.drawOn(c, content_x, node_y - mh + 2)
        item_y = node_y - mh

        # Role
        p_role.drawOn(c, content_x, item_y - rh_r - 1)
        item_y -= (rh_r + 3)

        # Bullets
        for p_b, bh in bullets:
            p_b.drawOn(c, content_x, item_y - bh)
            item_y -= (bh + 2)

    ry = item_y - 10

    # References Section
    right_heading("References")

    ref_w = (rw - 12) / 2
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(rx, ry, "Department of EEE")
    c.drawString(rx + ref_w + 12, ry, "Academic References")
    ry -= 11

    c.setFont("Helvetica", 7.5)
    c.setFillColor(TEXT_MUTED)
    c.drawString(rx, ry, "Jamalpur Science & Technology University (JSTU)")
    c.drawString(rx + ref_w + 12, ry, "Available Upon Request")
    ry -= 9.5
    c.drawString(rx, ry, "Phone: +880 1575 151636")
    c.drawString(rx + ref_w + 12, ry, "Email: yeasinbhuiyan265@gmail.com")
    ry -= 9.5
    c.drawString(rx, ry, "Email: info@jstu.edu.bd")
    c.drawString(rx + ref_w + 12, ry, "Portfolio: http://localhost:5500")

    c.save()
    print("Regenerated polished CV PDF:", pdf_path)

if __name__ == "__main__":
    create_cv()
