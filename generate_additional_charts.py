import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs('assets', exist_ok=True)
plt.rcParams['font.sans-serif'] = 'Helvetica', 'Arial', 'DejaVu Sans'

# 1. Architecture Blueprint Diagram
fig, ax = plt.subplots(figsize=(10, 5.5))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Layer boxes
layers = [
    ("1. DATA INGESTION & EXTERNAL TELEMETRY LAYER", 80, 16, '#1e3a8a', [
        "Marg ERP / Tally Connectors (SFTP / Webhook)",
        "IMD Gridded Rainfall API & CWC River Gauges",
        "ASDMA Disaster & Road Landslide Feeds",
        "IDSP Epidemiological Surveillance Feeds"
    ]),
    ("2. STREAMING, VALIDATION & TIME-SERIES STORAGE LAYER", 60, 16, '#0f766e', [
        "Apache Kafka / Celery Ingestion Bus",
        "Data Cleansing & ABC-VED Categorization",
        "PostgreSQL + TimescaleDB (Time-Series Dispatches)",
        "PostGIS (Geospatial Corridor Routing)"
    ]),
    ("3. CORE AI/ML PREDICTIVE & OPTIMIZATION LAYER", 40, 16, '#2563eb', [
        "Temporal Fusion Transformer (TFT) Multi-Horizon Forecast",
        "Quantile Loss Estimation (P10, P50, P90 Scenarios)",
        "Google OR-Tools MILP Multi-Echelon Rebalancer (MEIO)",
        "Graph-Theoretic FEFO Expiry Arbitrage Engine"
    ]),
    ("4. APPLICATION, SECURITY & INTEGRATION LAYER", 20, 16, '#d97706', [
        "FastAPI High-Throughput REST APIs & Redis Cache",
        "Role-Based Access Control (RBAC) & AES-256 Vault",
        "DPDP Act 2023 & CDSCO GxP Audit Log Engine",
        "Dhanuka Core ERP Purchase Order Sync Adapter"
    ]),
    ("5. PRESENTATION & MULTI-TIER USER INTERFACES", 0, 16, '#475569', [
        "Executive Web Command Portal (GIS Radar & Studio)",
        "Stockist Regional Replenishment Workbench",
        "Offline-First Progressive Web App (IndexedDB)",
        "Bilingual WhatsApp & SMS Conversational Bot"
    ])
]

for title, y, h, col, items in layers:
    # Outer box
    rect = patches.FancyBboxPatch((4, y), 92, h-2, boxstyle="round,pad=0.5", ec=col, fc='#f8fafc', lw=1.5)
    ax.add_patch(rect)
    # Header tag
    tag = patches.FancyBboxPatch((4, y+h-5.5), 92, 3.5, boxstyle="round,pad=0.2", ec="none", fc=col)
    ax.add_patch(tag)
    ax.text(6, y+h-3.8, title, color='white', fontsize=8.5, fontweight='bold', va='center')
    # Items
    for idx, item in enumerate(items):
        ix = 6 + (idx % 2) * 46
        iy = y + 7 - (idx // 2) * 4.2
        ax.text(ix, iy, f"• {item}", color='#1e293b', fontsize=7.5, va='center')

# Arrows connecting layers
for y in [78, 58, 38, 18]:
    ax.annotate('', xy=(50, y), xytext=(50, y+2),
                arrowprops=dict(facecolor='#64748b', edgecolor='none', width=1.5, headwidth=6))

plt.title("MediFlow-NE: End-to-End Enterprise Solution Architecture Blueprint", fontsize=11, fontweight='bold', pad=10, color='#0f172a')
plt.tight_layout()
plt.savefig('assets/architecture_diagram.png', dpi=300)
plt.close()

# 2. Multi-tier Distribution Network Flowchart
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Tier 1
t1 = patches.FancyBboxPatch((35, 78), 30, 16, boxstyle="round,pad=0.5", ec='#1e3a8a', fc='#dbeafe', lw=2)
ax.add_patch(t1)
ax.text(50, 87, "TIER 1: GUWAHATI CENTRAL C&F DEPOT", ha='center', va='center', fontweight='bold', fontsize=8.5, color='#1e3a8a')
ax.text(50, 82, "G.R. Dhanuka Complex / Athgaon\nCentral Inventory & ERP Command", ha='center', va='center', fontsize=7.5, color='#334155')

# Corridors
ax.annotate("NH-27 (Upper Assam)\nNormal Transit (3-5 Days)", xy=(25, 54), xytext=(40, 78),
            arrowprops=dict(facecolor='#10b981', edgecolor='none', width=1.5, headwidth=6),
            fontsize=7, ha='center', color='#065f46', fontweight='bold')

ax.annotate("NH-6 via Meghalaya\nHIGH FLOOD HAZARD (18-25 Days)", xy=(50, 54), xytext=(50, 78),
            arrowprops=dict(facecolor='#ef4444', edgecolor='none', width=2, headwidth=7),
            fontsize=7, ha='center', color='#991b1b', fontweight='bold')

ax.annotate("NH-29 to Nagaland/Manipur\nLandslide Prone (8-14 Days)", xy=(75, 54), xytext=(60, 78),
            arrowprops=dict(facecolor='#f59e0b', edgecolor='none', width=1.5, headwidth=6),
            fontsize=7, ha='center', color='#92400e', fontweight='bold')

# Tier 2
t2_a = patches.FancyBboxPatch((12, 38), 24, 14, boxstyle="round,pad=0.4", ec='#0f766e', fc='#ccfbf1', lw=1.5)
ax.add_patch(t2_a)
ax.text(24, 46, "DIBRUGARH / TEZPUR", ha='center', va='center', fontweight='bold', fontsize=8, color='#0f766e')
ax.text(24, 41, "Upper Assam Staging Hubs\nBuffer: 21 Days", ha='center', va='center', fontsize=7, color='#334155')

t2_b = patches.FancyBboxPatch((38, 38), 24, 14, boxstyle="round,pad=0.4", ec='#b91c1c', fc='#fee2e2', lw=2)
ax.add_patch(t2_b)
ax.text(50, 46, "SILCHAR BUFFER DEPOT", ha='center', va='center', fontweight='bold', fontsize=8, color='#b91c1c')
ax.text(50, 41, "Barak Valley Pre-Positioning\nBuffer: 35-45 Days (Monsoon)", ha='center', va='center', fontsize=7, color='#334155')

t2_c = patches.FancyBboxPatch((64, 38), 24, 14, boxstyle="round,pad=0.4", ec='#b45309', fc='#fef3c7', lw=1.5)
ax.add_patch(t2_c)
ax.text(76, 46, "DIMAPUR / KOHIMA", ha='center', va='center', fontweight='bold', fontsize=8, color='#b45309')
ax.text(76, 41, "Hill Route Staging Node\nBuffer: 28 Days", ha='center', va='center', fontsize=7, color='#334155')

# Tier 3 & 4
t3 = patches.FancyBboxPatch((10, 6), 80, 20, boxstyle="round,pad=0.5", ec='#64748b', fc='#f8fafc', lw=1.5)
ax.add_patch(t3)
ax.text(50, 21, "TIERS 3 & 4: PERIPHERAL CHEMISTS, PHCS & COMMUNITY HEALTH CENTRES", ha='center', va='center', fontweight='bold', fontsize=8.5, color='#1e293b')
ax.text(50, 14, "Connected via Offline-First PWA & WhatsApp Bot • Daily Stock Depletion Sync • Dynamic Emergency Indenting\nGuaranteed Zero-Stockout for Anti-Snake Venom, Cold-Chain Insulin, and Pediatric Antibiotics", ha='center', va='center', fontsize=7.5, color='#475569')

for x in [24, 50, 76]:
    ax.annotate('', xy=(x, 26), xytext=(x, 38),
                arrowprops=dict(facecolor='#64748b', edgecolor='none', width=1.2, headwidth=5))

plt.title("Northeast India Multi-Tier Pharmaceutical Distribution & Flood Hazard Network", fontsize=11, fontweight='bold', pad=10, color='#0f172a')
plt.tight_layout()
plt.savefig('assets/multi_tier_network.png', dpi=300)
plt.close()

# 3. FEFO Expiry Arbitrage Flowchart
fig, ax = plt.subplots(figsize=(9, 4.5))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Origin
b1 = patches.FancyBboxPatch((8, 55), 34, 32, boxstyle="round,pad=0.5", ec='#f59e0b', fc='#fef3c7', lw=1.5)
ax.add_patch(b1)
ax.text(25, 80, "SLOW-MOVING SUB-DEPOT", ha='center', fontweight='bold', fontsize=8.5, color='#92400e')
ax.text(25, 73, "Example: Tezpur Sub-Stockist", ha='center', fontsize=7.5, color='#78350f')
ax.text(25, 65, "Batch #ARB-204 (Rabies Serum)\n• Stock: 180 Vials\n• Expiry: 4.5 Months\n• Depletion Velocity: 4 vials/mo", ha='center', fontsize=7.2, color='#451a03')
ax.text(25, 57, "[Projected Expiry Loss: ₹1.44 Lakhs]", ha='center', fontweight='bold', fontsize=7.2, color='#b91c1c')

# Destination
b2 = patches.FancyBboxPatch((58, 55), 34, 32, boxstyle="round,pad=0.5", ec='#10b981', fc='#ecfdf5', lw=1.5)
ax.add_patch(b2)
ax.text(75, 80, "HIGH-CONSUMPTION HUB", ha='center', fontweight='bold', fontsize=8.5, color='#065f46')
ax.text(75, 73, "Example: Silchar Civil Hospital", ha='center', fontsize=7.5, color='#047857')
ax.text(75, 65, "Emergency Intake Ward\n• Current Stock: 8 Vials (Critical)\n• Depletion Velocity: 90 vials/mo\n• Stockout Hazard: 92%", ha='center', fontsize=7.2, color='#064e3b')
ax.text(75, 57, "[Patient Need: Urgent Life-Saving]", ha='center', fontweight='bold', fontsize=7.2, color='#0f766e')

# Transfer arrow with label
ax.annotate('', xy=(58, 71), xytext=(42, 71),
            arrowprops=dict(facecolor='#2563eb', edgecolor='none', width=2.5, headwidth=8))
ax.text(50, 76, "FEFO REBALANCE", ha='center', va='center', fontweight='bold', fontsize=7.5, color='#1d4ed8')
ax.text(50, 66, "Algorithmic Gate Pass\n160 Vials Transferred", ha='center', va='center', fontsize=7, color='#1e40af')

# Result Box
res = patches.FancyBboxPatch((15, 10), 70, 30, boxstyle="round,pad=0.5", ec='#1e3a8a', fc='#f8fafc', lw=1.5)
ax.add_patch(res)
ax.text(50, 33, "SYSTEM OUTCOME OF ALGORITHMIC ARBITRAGE", ha='center', fontweight='bold', fontsize=9, color='#1e3a8a')
ax.text(50, 26, "[OK] 100% Expiry Salvage: All 160 vials fully consumed 3 months before expiry date.", ha='center', fontsize=7.8, color='#065f46', fontweight='bold')
ax.text(50, 20, "[OK] Zero Stockout: Silchar emergency hospital stock maintained at safe operational buffer.", ha='center', fontsize=7.8, color='#065f46', fontweight='bold')
ax.text(50, 14, "[OK] Financial Optimization: Avoided write-offs + eliminated emergency express freight surcharge.", ha='center', fontsize=7.8, color='#1e293b')

plt.title("Cross-Tier Expiry Arbitrage & FEFO Stock Rebalancing Mechanism", fontsize=11, fontweight='bold', pad=10, color='#0f172a')
plt.tight_layout()
plt.savefig('assets/arbitrage_flow.png', dpi=300)
plt.close()

print("Additional visual charts generated successfully.")
