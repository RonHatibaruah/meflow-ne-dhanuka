with open("generate_pdf.py") as f:
    code = f.read()

# Replace budget breakdown image
code = code.replace("if os.path.exists('assets/budget_breakdown.png'):\n        story.append(Image('assets/budget_breakdown.png', width=450, height=270))",
                    "if os.path.exists('assets/infographic_06_budget_allocation.jpg'):\n        story.append(Image('assets/infographic_06_budget_allocation.jpg', width=470, height=263))\n    elif os.path.exists('assets/budget_breakdown.png'):\n        story.append(Image('assets/budget_breakdown.png', width=450, height=270))")

# Replace multi_tier_network image
code = code.replace("if os.path.exists('assets/multi_tier_network.png'):\n        story.append(Image('assets/multi_tier_network.png', width=450, height=225))",
                    "if os.path.exists('assets/infographic_01_supply_network.jpg'):\n        story.append(Image('assets/infographic_01_supply_network.jpg', width=470, height=263))\n    elif os.path.exists('assets/multi_tier_network.png'):\n        story.append(Image('assets/multi_tier_network.png', width=450, height=225))")

# Replace architecture_diagram image
code = code.replace("if os.path.exists('assets/architecture_diagram.png'):\n        story.append(Image('assets/architecture_diagram.png', width=450, height=245))",
                    "if os.path.exists('assets/infographic_02_solution_architecture.jpg'):\n        story.append(Image('assets/infographic_02_solution_architecture.jpg', width=470, height=263))\n    elif os.path.exists('assets/architecture_diagram.png'):\n        story.append(Image('assets/architecture_diagram.png', width=450, height=245))")

# Replace arbitrage_flow image
code = code.replace("if os.path.exists('assets/arbitrage_flow.png'):\n        story.append(Image('assets/arbitrage_flow.png', width=450, height=225))",
                    "if os.path.exists('assets/infographic_03_expiry_arbitrage.jpg'):\n        story.append(Image('assets/infographic_03_expiry_arbitrage.jpg', width=470, height=263))\n    elif os.path.exists('assets/arbitrage_flow.png'):\n        story.append(Image('assets/arbitrage_flow.png', width=450, height=225))")

# Replace simulation_timeline image
code = code.replace("if os.path.exists('assets/simulation_timeline.png'):\n        story.append(Image('assets/simulation_timeline.png', width=450, height=230))",
                    "if os.path.exists('assets/infographic_04_flood_simulation.jpg'):\n        story.append(Image('assets/infographic_04_flood_simulation.jpg', width=470, height=263))\n    elif os.path.exists('assets/simulation_timeline.png'):\n        story.append(Image('assets/simulation_timeline.png', width=450, height=230))")

# Replace cold_chain_iot image
code = code.replace("if os.path.exists('assets/cold_chain_iot.png'):\n        story.append(Image('assets/cold_chain_iot.png', width=450, height=215))",
                    "if os.path.exists('assets/infographic_05_cold_chain_iot.jpg'):\n        story.append(Image('assets/infographic_05_cold_chain_iot.jpg', width=470, height=263))\n    elif os.path.exists('assets/cold_chain_iot.png'):\n        story.append(Image('assets/cold_chain_iot.png', width=450, height=215))")

# Replace user_persona_matrix image
code = code.replace("if os.path.exists('assets/user_persona_matrix.png'):\n        story.append(Image('assets/user_persona_matrix.png', width=450, height=215))",
                    "if os.path.exists('assets/infographic_07_user_personas.jpg'):\n        story.append(Image('assets/infographic_07_user_personas.jpg', width=470, height=263))\n    elif os.path.exists('assets/user_persona_matrix.png'):\n        story.append(Image('assets/user_persona_matrix.png', width=450, height=215))")

# Replace timeline_gantt image
code = code.replace("if os.path.exists('assets/timeline_gantt.png'):\n        story.append(Image('assets/timeline_gantt.png', width=450, height=190))",
                    "if os.path.exists('assets/infographic_08_implementation_roadmap.jpg'):\n        story.append(Image('assets/infographic_08_implementation_roadmap.jpg', width=470, height=263))\n    elif os.path.exists('assets/timeline_gantt.png'):\n        story.append(Image('assets/timeline_gantt.png', width=450, height=190))")

with open("generate_pdf.py", "w") as f:
    f.write(code)

print("generate_pdf.py updated with Gemini Pro 16:9 infographics.")
