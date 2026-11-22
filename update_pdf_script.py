with open("generate_pdf.py") as f:
    code = f.read()

# Add new images to Part 3 of the PDF
old_pow_text = """    story.append(Paragraph("PART 3: PROOF OF WORK (POW) & BENCHMARK EVIDENCE", h1_style))
    story.append(Paragraph("To satisfy the mandatory requirement that a proposal narrative alone is insufficient, this section presents empirical simulation results, forecasting model comparisons, architectural blueprints, and screen wireframes.", body_style))
    story.append(Spacer(1, 6))"""

new_pow_text = """    story.append(Paragraph("PART 3: PROOF OF WORK (POW) & BENCHMARK EVIDENCE", h1_style))
    story.append(Paragraph("To satisfy the mandatory requirement that a proposal narrative alone is insufficient, this section presents empirical simulation results, forecasting model comparisons, architectural blueprints, and screen wireframes.", body_style))
    story.append(Spacer(1, 6))

    story.append(Paragraph("1. Regional Multi-Tier Supply Chain & Corridor Vulnerability Map", h2_style))
    story.append(Paragraph("The diagram below illustrates the hierarchical flow from G.R. Dhanuka Group central C&F hubs to district staging depots and remote health facilities across Northeast India, highlighting high-hazard flood corridors (e.g. NH-6 via Meghalaya).", body_style))
    story.append(Spacer(1, 4))
    if os.path.exists('assets/multi_tier_network.png'):
        story.append(Image('assets/multi_tier_network.png', width=450, height=225))
        story.append(Spacer(1, 8))

    story.append(Paragraph("2. Enterprise Solution Architecture Blueprint", h2_style))
    story.append(Paragraph("The platform connects legacy stockist ERPs (Marg, Tally, Busy) and real-time environmental APIs (IMD, CWC, ASDMA) to our cloud-native AI forecasting and optimization pipeline.", body_style))
    story.append(Spacer(1, 4))
    if os.path.exists('assets/architecture_diagram.png'):
        story.append(Image('assets/architecture_diagram.png', width=450, height=245))
        story.append(Spacer(1, 8))

    story.append(Paragraph("3. Cross-Tier Expiry Arbitrage & FEFO Rebalancing Mechanism", h2_style))
    story.append(Paragraph("Graph-theoretic matching re-routes near-expiry batches from slow-moving nodes to high-velocity emergency wards, eliminating waste and averting stockouts.", body_style))
    story.append(Spacer(1, 4))
    if os.path.exists('assets/arbitrage_flow.png'):
        story.append(Image('assets/arbitrage_flow.png', width=450, height=225))
        story.append(Spacer(1, 8))"""

code = code.replace(old_pow_text, new_pow_text)

# Also update the numbering for model benchmark from 1 to 4, simulation from 2 to 5, timeline from 3 to 6
code = code.replace("story.append(Paragraph(\"1. Model Performance Benchmark: TFT vs Conventional Forecasting\", h2_style))",
                    "story.append(Paragraph(\"4. Model Performance Benchmark: TFT vs Conventional Forecasting\", h2_style))")
code = code.replace("story.append(Paragraph(\"2. Discrete-Event Highway Corridor Flood Simulation",
                    "story.append(Paragraph(\"5. Discrete-Event Highway Corridor Flood Simulation")
code = code.replace("story.append(Paragraph(\"3. 12-Month Phased Implementation Roadmap\", h2_style))",
                    "story.append(Paragraph(\"6. 12-Month Phased Implementation Roadmap\", h2_style))")

with open("generate_pdf.py", "w") as f:
    f.write(code)

print("generate_pdf.py updated successfully.")
