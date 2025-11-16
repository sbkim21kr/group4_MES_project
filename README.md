# Group 4 MES Project

A modular, multi-layered Manufacturing Execution System (MES) framework integrating Dobot robotic arms, PLCs, SCADA, and KPI analytics. Built for educational and industrial automation scenarios.

---

## 📦 Project Structure

```
group4-mes-project/
│
├── pyproject.toml         # Project metadata and dependencies
├── uv.lock                # uv lockfile for reproducible environments
├── .venv/                 # Virtual environment (auto-managed by uv)
│
├── robots/                # Robotic control layer
│   ├── controller.py      # Shared base class for Dobot control
│   ├── dobot_com3.py      # Dobot instance on COM3 with motion profiles
│   ├── dobot_com4.py      # Additional Dobot instances (COM4–COM6)
│   └── __init__.py
│
├── sdk/                   # Dobot SDK bindings
│   ├── DobotAPI.py
│   ├── DobotControl.py
│   ├── DobotDll.dll
│   ├── DobotSession.py
│   └── DobotTypes.py
│
├── plc/                   # PLC interface layer
│   ├── melsec_interface.py
│   └── __init__.py
│
├── scada/                 # SCADA bridge and data storage
│   ├── scada_bridge.py
│   ├── sqlite_store.py
│   └── __init__.py
│
├── orchestrator/          # System-level coordination and scheduling
│   ├── scheduler.py
│   ├── system_manager.py
│   └── __init__.py
│
├── dashboard/             # Visualization and UI layer
│   ├── app.py
│   └── __init__.py
│
└── sprodis/               # KPI comparison and export tools
    ├── kpi_compare.py
    ├── kpi_export.py
    └── __init__.py
```

---

## 🤖 Dobot Motion Control

The `robots/dobot_com3.py` script demonstrates:

- Safe home positioning
- Dynamic motion profiles (fast travel, slow approach, gentle retreat)
- Suction control for pick-and-place
- Layered Z-axis palletizing logic

### Motion Profiles

```python
self.fast_speed = (100, 100)
self.slow_speed = (30, 30)
self.retreat_speed = (50, 50)
```

These are applied using:

```python
self.set_motion_profile(*self.fast_speed)
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/group4-mes-project.git
cd group4-mes-project
```

### 2. Initialize the environment with `uv`

```bash
uv init
uv venv
```

### 3. Run the Dobot script

```bash
python robots/dobot_com3.py
```

Make sure your Dobot is connected (e.g., COM3) and powered on.

---

## 📌 Requirements

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) for environment management
- Dobot SDK and DLL (included in `sdk/`)
- Dobot Magician hardware + USB connection

---

## 🛠️ In Progress

- PLC integration via MELSEC
- SCADA bridge and real-time data logging
- KPI dashboard and export tools
- Multi-arm coordination (COM3–COM6)

