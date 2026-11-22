with open("generate_pdf.py") as f:
    code = f.read()

# Locate where Section 5 (Discrete-Event simulation) is in Part 3
old_sim_text = """    story.append(Paragraph("5. Discrete-Event Highway Corridor Flood Simulation (Guwahati -> Silchar / Barak Valley)", h2_style))
    story.append(Paragraph("We simulated a realistic 21-day washout scenario along NH-6 (connecting Guwahati through Meghalaya into Barak Valley, Tripura, and Mizoram) during peak July monsoon. Under standard heuristics, retail pharmacies experienced catastrophic stockouts (41.8% stockout rate). MediFlow-NE’s proactive pre-positioning triggered 14 days prior maintained a 94.6% in-stock service level throughout the isolation period.", body_style))
    story.append(Spacer(1, 8))"""

new_sim_text = """    story.append(Paragraph("5. Discrete-Event Highway Corridor Flood Simulation (Guwahati -> Silchar / Barak Valley)", h2_style))
    story.append(Paragraph("We simulated a realistic 21-day washout scenario along NH-6 (connecting Guwahati through Meghalaya into Barak Valley, Tripura, and Mizoram) during peak July monsoon. Under standard heuristics, retail pharmacies experienced catastrophic stockouts (41.8% stockout rate). MediFlow-NE’s proactive pre-positioning triggered 14 days prior maintained a 94.6% in-stock service level throughout the isolation period.", body_style))
    story.append(Spacer(1, 4))
    if os.path.exists('assets/simulation_timeline.png'):
        story.append(Image('assets/simulation_timeline.png', width=450, height=230))
        story.append(Spacer(1, 8))

    story.append(Paragraph("6. Cold-Chain IoT Architecture for Temperature-Sensitive Biologics (2°C–8°C)", h2_style))
    story.append(Paragraph("Vital formulations like Insulin, Anti-Snake Venom, and pediatric vaccines require continuous thermal integrity. MediFlow-NE incorporates cellular IoT telemetry, automated transit excursion flags, and instant batch quarantine locks in connected billing ERPs.", body_style))
    story.append(Spacer(1, 4))
    if os.path.exists('assets/cold_chain_iot.png'):
        story.append(Image('assets/cold_chain_iot.png', width=450, height=215))
        story.append(Spacer(1, 8))

    story.append(Paragraph("7. Multi-Tier Interface Architecture Across User Personas", h2_style))
    story.append(Paragraph("The platform delivers tailored, frictionless touchpoints across the entire supply hierarchy—from Central C&F dispatchers down to rural village chemists and cut-off PHC pharmacists.", body_style))
    story.append(Spacer(1, 4))
    if os.path.exists('assets/user_persona_matrix.png'):
        story.append(Image('assets/user_persona_matrix.png', width=450, height=215))
        story.append(Spacer(1, 8))"""

code = code.replace(old_sim_text, new_sim_text)
code = code.replace("story.append(Paragraph(\"6. 12-Month Phased Implementation Roadmap\", h2_style))",
                    "story.append(Paragraph(\"8. 12-Month Phased Implementation Roadmap\", h2_style))")

with open("generate_pdf.py", "w") as f:
    f.write(code)

print("generate_pdf.py updated with all evaluator figures.")
