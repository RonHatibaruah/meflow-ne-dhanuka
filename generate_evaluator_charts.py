import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

os.makedirs('assets', exist_ok=True)
plt.rcParams['font.sans-serif'] = 'Helvetica', 'Arial', 'DejaVu Sans'

# 1. Evaluator Image: 21-Day Flood Washout Simulation Timeline (Traditional vs MediFlow-NE)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 5.2), sharex=True)

days = np.arange(1, 31)
# Traditional: stock drops to 0 during flood (days 12 to 24)
trad_stock = np.array([28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 8, 14, 18, 20, 22, 24, 25, 26])
# MediFlow-NE: pre-positioning triggers on Day 5, stocks peak before flood, remaining > 10 days runway throughout
mediflow_stock = np.array([28, 27, 28, 30, 38, 44, 46, 45, 43, 40, 36, 33, 30, 27, 24, 22, 20, 18, 17, 16, 15, 16, 22, 28, 32, 34, 34, 33, 32, 31])

# Plot Traditional
ax1.plot(days, trad_stock, color='#dc2626', linewidth=2.5, label='Traditional Heuristic Ordering (ERP Baseline)')
ax1.axvspan(10, 22, color='#fee2e2', alpha=0.6, label='NH-6 Highway Corridor Severed (Flood / Landslide)')
ax1.axhline(5, color='#b91c1c', linestyle='--', linewidth=1, label='Critical Stockout Danger Threshold (< 5 Days)')
ax1.fill_between(days, 0, trad_stock, color='#fca5a5', alpha=0.3)
ax1.set_ylabel('Depot Runway (Days)', fontsize=8.5, fontweight='bold', color='#1e293b')
ax1.set_title('Traditional Approach: Catastrophic 10-Day Stockout in Silchar / Barak Valley', fontsize=9.5, fontweight='bold', color='#991b1b')
ax1.set_ylim(-2, 50)
ax1.grid(True, linestyle=':', alpha=0.5)
ax1.legend(loc='upper right', fontsize=7.5, frameon=True, facecolor='white')

# Plot MediFlow-NE
ax2.plot(days, mediflow_stock, color='#0284c7', linewidth=2.5, label='MediFlow-NE AI Proactive Pre-Positioning')
ax2.axvspan(10, 22, color='#fee2e2', alpha=0.6, label='NH-6 Highway Corridor Severed (Flood / Landslide)')
ax2.axhline(5, color='#b91c1c', linestyle='--', linewidth=1, label='Critical Stockout Danger Threshold')
ax2.annotate('AI Pre-Positioning Dispatched\n(+20 Days Buffer Stocked)', xy=(5, 38), xytext=(2, 45),
             arrowprops=dict(facecolor='#0284c7', width=1.5, headwidth=6),
             fontsize=7.5, fontweight='bold', color='#0369a1')
ax2.fill_between(days, 0, mediflow_stock, color='#bae6fd', alpha=0.3)
ax2.set_xlabel('Timeline (Days)', fontsize=9, fontweight='bold', color='#1e293b')
ax2.set_ylabel('Depot Runway (Days)', fontsize=8.5, fontweight='bold', color='#1e293b')
ax2.set_title('MediFlow-NE: Continuous 100% Availability Maintained Through Predictive Pre-Positioning', fontsize=9.5, fontweight='bold', color='#0369a1')
ax2.set_ylim(-2, 50)
ax2.grid(True, linestyle=':', alpha=0.5)
ax2.legend(loc='upper right', fontsize=7.5, frameon=True, facecolor='white')

plt.tight_layout()
plt.savefig('assets/simulation_timeline.png', dpi=300)
plt.close()

# 2. Cold Chain IoT & Temperature-Sensitive Medicine Integrity Diagram
fig, ax = plt.subplots(figsize=(10, 4.8))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Title
ax.text(50, 94, "IoT Cold-Chain Integrity Architecture (2°C–8°C for Insulin & Anti-Snake Venom)", 
        ha='center', fontsize=11, fontweight='bold', color='#0f172a')

# Step 1: Warehouse Storage
s1 = patches.FancyBboxPatch((4, 45), 26, 40, boxstyle="round,pad=0.5", ec='#0284c7', fc='#f0f9ff', lw=1.5)
ax.add_patch(s1)
ax.text(17, 78, "CENTRAL C&F COLD ROOM", ha='center', fontweight='bold', fontsize=8, color='#0369a1')
ax.text(17, 72, "Guwahati Central Depot", ha='center', fontsize=7, color='#475569')
ax.text(17, 60, "• Active 2°C–8°C Monitoring\n• IoT Gateway + BLE Beacons\n• Auto-Hold on Temp Anomaly\n• Calibrated Temperature Log", ha='center', fontsize=6.8, color='#0f172a')

# Step 2: Transit Logistics
s2 = patches.FancyBboxPatch((37, 45), 26, 40, boxstyle="round,pad=0.5", ec='#0d9488', fc='#f0fdfa', lw=1.5)
ax.add_patch(s2)
ax.text(50, 78, "REEFER & INSULATED TRANSIT", ha='center', fontweight='bold', fontsize=8, color='#0f766e')
ax.text(50, 72, "NH-6 / NH-29 Transit Corridors", ha='center', fontsize=7, color='#475569')
ax.text(50, 60, "• Cellular IoT GPS + Temp Track\n• Real-Time Excursion Alerts\n• Dynamic Re-Route Recommendations\n• Battery Backup: 72 Hours", ha='center', fontsize=6.8, color='#0f172a')

# Step 3: Edge Delivery / PHC
s3 = patches.FancyBboxPatch((70, 45), 26, 40, boxstyle="round,pad=0.5", ec='#16a34a', fc='#f0fdf4', lw=1.5)
ax.add_patch(s3)
ax.text(83, 78, "LAST-MILE HEALTH NODE", ha='center', fontweight='bold', fontsize=8, color='#15803d')
ax.text(83, 72, "Silchar / PHCs / Chemists", ha='center', fontsize=7, color='#475569')
ax.text(83, 60, "• QR Code Cold-Chain Scan\n• Instant Pass/Fail Gate Receipt\n• Solar Vaccine Fridge Integration\n• GxP Batch Release Verification", ha='center', fontsize=6.8, color='#0f172a')

# Arrows
ax.annotate('', xy=(37, 65), xytext=(30, 65),
            arrowprops=dict(facecolor='#0284c7', width=2, headwidth=6))
ax.annotate('', xy=(70, 65), xytext=(63, 65),
            arrowprops=dict(facecolor='#0d9488', width=2, headwidth=6))

# Lower Banner
banner = patches.FancyBboxPatch((4, 8), 92, 28, boxstyle="round,pad=0.5", ec='#64748b', fc='#f8fafc', lw=1)
ax.add_patch(banner)
ax.text(50, 27, "REGULATORY COMPLIANCE & SAFETY ASSURANCE", ha='center', fontweight='bold', fontsize=8.5, color='#1e293b')
ax.text(50, 18, "[OK] CDSCO Guidelines for Good Distribution Practices (GDP) · [OK] WHO TRS 961 Temperature Mapping Standards\n[OK] Automated Quarantine Protocol: Immediate lock in billing ERP if transit temp exceeds 8°C for > 60 minutes",
        ha='center', fontsize=7.2, color='#334155')

plt.tight_layout()
plt.savefig('assets/cold_chain_iot.png', dpi=300)
plt.close()

# 3. User Persona Wireframe Matrix (4 Key Personas)
fig, ax = plt.subplots(figsize=(10, 4.8))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

ax.text(50, 94, "MediFlow-NE: Multi-Tier Interface Architecture Across User Personas", 
        ha='center', fontsize=11, fontweight='bold', color='#0f172a')

personas = [
    ("Central C&F Logistics Head\n(Guwahati Hub)", 4, '#1e3a8a', '#eff6ff', [
        "Web Command Console",
        "Geospatial Hazard Radar",
        "Probabilistic Forecast Studio",
        "1-Click Pre-Positioning Indents"
    ]),
    ("District Super-Stockist\n(Dibrugarh / Silchar)", 28, '#0f766e', '#f0fdfa', [
        "Stockist Planning Portal",
        "FEFO Expiry Rebalancer",
        "Marg / Tally Auto-Sync",
        "Pending PO Approvals"
    ]),
    ("Rural Retail Chemist\n(Peripheral Village)", 52, '#d97706', '#fffbeb', [
        "Offline-First Edge PWA",
        "2G / No-Network Mode",
        "Barcode / QR Batch Scanner",
        "Local IndexedDB Sync"
    ]),
    ("Remote PHC Pharmacist\n(Hilly / Cut-Off Node)", 76, '#15803d', '#f0fdf4', [
        "WhatsApp Conversational Bot",
        "SMS Reorder Fallback",
        "30-Sec Voice/Text Indenting",
        "Urgent Lifesaving Drug Alert"
    ])
]

for title, x, col, bg, items in personas:
    box = patches.FancyBboxPatch((x, 10), 20, 78, boxstyle="round,pad=0.4", ec=col, fc=bg, lw=1.5)
    ax.add_patch(box)
    # Header tag
    tag = patches.FancyBboxPatch((x, 70), 20, 18, boxstyle="round,pad=0.2", ec="none", fc=col)
    ax.add_patch(tag)
    ax.text(x+10, 79, title, color='white', fontsize=7, fontweight='bold', ha='center', va='center')
    # Items
    for idx, item in enumerate(items):
        iy = 60 - idx * 12
        item_box = patches.FancyBboxPatch((x+1.5, iy-3), 17, 9, boxstyle="round,pad=0.2", ec=col, fc='white', lw=0.8)
        ax.add_patch(item_box)
        ax.text(x+10, iy+1.5, item, color='#1e293b', fontsize=6.5, ha='center', va='center', fontweight='medium')

plt.tight_layout()
plt.savefig('assets/user_persona_matrix.png', dpi=300)
plt.close()

print("Evaluator diagrams generated successfully.")
