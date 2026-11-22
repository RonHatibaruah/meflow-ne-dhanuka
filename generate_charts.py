import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

os.makedirs('assets', exist_ok=True)
plt.rcParams['font.sans-serif'] = 'Helvetica', 'Arial', 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cbd5e1'
plt.rcParams['axes.linewidth'] = 0.8

# 1. Budget Breakdown Chart
labels = [
    'Technical Engineering Team\n(Core Fullstack & Data Engineers)\n₹20.00 L (50.0%)',
    'AI/ML Predictive Models &\nWeather/Geo Pipelines\n₹6.50 L (16.25%)',
    'Field Pilot & Stockist Onboarding\n(Guwahati, Dibrugarh, Silchar)\n₹5.00 L (12.50%)',
    'Cloud Infra, Edge Sync &\nHigh-Availability Hosting\n₹4.50 L (11.25%)',
    'QA, Security Audit, GxP/CDSCO\nCompliance & Contingency\n₹4.00 L (10.00%)'
]
amounts = [20.0, 6.5, 5.0, 4.5, 4.0]
colors = ['#1e3a8a', '#0284c7', '#0d9488', '#f59e0b', '#64748b']

fig, ax = plt.subplots(figsize=(8, 4.8), subplot_kw=dict(aspect="equal"))
wedges, texts, autotexts = ax.pie(
    amounts, 
    labels=labels, 
    autopct='%1.1f%%',
    pctdistance=0.75,
    colors=colors,
    startangle=140,
    textprops=dict(color="#1e293b", fontsize=9, fontweight='medium'),
    wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2)
)
for at in autotexts:
    at.set_color('white')
    at.set_fontweight('bold')
    at.set_fontsize(9)
ax.set_title("NESFIC-I-09 Indicative Budget Allocation (Total Grant: ₹40.00 Lakhs)", fontsize=12, fontweight='bold', pad=15, color='#0f172a')
plt.tight_layout()
plt.savefig('assets/budget_breakdown.png', dpi=300)
plt.close()

# 2. Forecast Performance Comparison (Baseline vs MediFlow-NE)
categories = ['Overall Medicine Demand\n(Aggregate)', 'Monsoon Epidemic SKUs\n(Antibiotics/IV Fluids)', 'Chronic Disease SKUs\n(Cardio / Diabetic)', 'Cold Chain Vaccines\n& Biologics', 'Stockout Rate at\nRemote Hill PHCs/Chemists']
traditional = [36.5, 48.2, 28.4, 34.0, 24.5]
mediflow = [11.2, 14.8, 8.6, 9.4, 4.2]

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(9, 4.6))
rects1 = ax.bar(x - width/2, traditional, width, label='Current Baseline (ERP / Manual Heuristics)', color='#94a3b8')
rects2 = ax.bar(x + width/2, mediflow, width, label='Proposed MediFlow-NE (TFT + MEIO Engine)', color='#2563eb')

ax.set_ylabel('Error Rate (MAPE %) / Stockout %', fontsize=10, fontweight='bold', color='#1e293b')
ax.set_title('Forecast Error (MAPE %) and Last-Mile Stockout Comparison', fontsize=12, fontweight='bold', pad=15, color='#0f172a')
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=8.5, color='#334155')
ax.legend(frameon=True, facecolor='#f8fafc', edgecolor='#cbd5e1')
ax.grid(axis='y', linestyle='--', alpha=0.5)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}%',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8, fontweight='bold')

autolabel(rects1)
autolabel(rects2)
plt.tight_layout()
plt.savefig('assets/forecast_performance.png', dpi=300)
plt.close()

# 3. Development Roadmap Gantt Chart
phases = [
    'Phase 1: Discovery & ERP Connector Design',
    'Phase 2: Core ML Engine & MEIO Development',
    'Phase 3: Multi-tier Dashboard & Offline Edge PWA',
    'Phase 4: Field Integration & Dhanuka Hub Pilot',
    'Phase 5: Full Evaluation, Security Audit & Scaling'
]
starts = [0, 2, 4, 7, 10]
durations = [2.5, 3.0, 3.5, 3.5, 2.0]
colors_gantt = ['#3b82f6', '#10b981', '#f59e0b', '#6366f1', '#ec4899']

fig, ax = plt.subplots(figsize=(9, 3.8))
for i in range(len(phases)):
    ax.barh(phases[i], durations[i], left=starts[i], color=colors_gantt[i], height=0.45, edgecolor='none')
    ax.text(starts[i] + durations[i]/2, i, f'M{starts[i]+1}-M{starts[i]+int(durations[i])}', 
            ha='center', va='center', color='white', fontweight='bold', fontsize=8.5)

ax.set_xlabel('Project Month (1 to 12)', fontsize=10, fontweight='bold', color='#1e293b')
ax.set_xlim(0, 12)
ax.set_xticks(range(0, 13))
ax.invert_yaxis()
ax.set_title('12-Month Phased Implementation Roadmap & Key Milestones', fontsize=12, fontweight='bold', pad=12, color='#0f172a')
ax.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('assets/timeline_gantt.png', dpi=300)
plt.close()

print('Charts generated successfully.')
