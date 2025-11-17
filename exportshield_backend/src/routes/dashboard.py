from fastapi import APIRouter
from datetime import datetime

router = APIRouter(prefix="/api/dashboard", tags=["Dashboard"])


@router.get("/statistics")
def get_dashboard_statistics():
    """Get comprehensive dashboard statistics for demo"""
    return {
        "overview": {
            "total_workers": 8,
            "active_workers": 6,
            "critical_workers": 1,
            "workers_on_break": 1,
            "total_machinery": 6,
            "operational_machinery": 5,
            "maintenance_required": 1,
            "total_incidents": 6,
            "active_incidents": 4,
            "resolved_incidents": 2,
            "total_corridors": 5,
            "safe_corridors": 3,
            "high_risk_corridors": 1,
        },
        "health_metrics": {
            "average_heart_rate": 86.25,
            "average_temperature": 37.64,
            "average_oxygen_level": 94.62,
            "workers_with_high_fatigue": 2,
            "workers_needing_medical_attention": 1,
        },
        "equipment_metrics": {
            "average_machinery_health": 83.0,
            "average_efficiency": 89.5,
            "high_risk_equipment": 1,
            "equipment_due_maintenance_soon": 2,
            "total_operating_hours": 10150,
        },
        "safety_metrics": {
            "incidents_today": 2,
            "incidents_this_week": 6,
            "high_severity_incidents": 3,
            "zones_requiring_attention": ["Zone A", "Zone B", "Zone C"],
            "safety_compliance_score": 78.5,
        },
        "environmental_metrics": {
            "average_pollution_level": 43.8,
            "average_green_cover": 25.6,
            "average_temperature": 27.4,
            "average_traffic_density": 51.0,
            "overall_compliance": 84.2,
        },
        "alerts": [
            {
                "id": "alert_1",
                "type": "critical",
                "message": "Worker Vikram Singh showing critical health signs in Zone A",
                "priority": "high",
                "timestamp": datetime.utcnow().isoformat() + "Z",
            },
            {
                "id": "alert_2",
                "type": "warning",
                "message": "Rotary Drill RD-2500 requires immediate maintenance",
                "priority": "high",
                "timestamp": datetime.utcnow().isoformat() + "Z",
            },
            {
                "id": "alert_3",
                "type": "warning",
                "message": "Tunnel collapse risk detected in Zone C - evacuation recommended",
                "priority": "critical",
                "timestamp": datetime.utcnow().isoformat() + "Z",
            },
            {
                "id": "alert_4",
                "type": "info",
                "message": "Ventilation system operating at optimal levels",
                "priority": "low",
                "timestamp": datetime.utcnow().isoformat() + "Z",
            },
        ],
        "recent_activity": [
            {
                "id": "activity_1",
                "type": "incident",
                "description": "Gas leak incident reported in Zone B",
                "timestamp": datetime.utcnow().isoformat() + "Z",
            },
            {
                "id": "activity_2",
                "type": "maintenance",
                "description": "Scheduled maintenance completed for Loader FL-800",
                "timestamp": datetime.utcnow().isoformat() + "Z",
            },
            {
                "id": "activity_3",
                "type": "worker",
                "description": "New worker Arjun Desai added to Zone D",
                "timestamp": datetime.utcnow().isoformat() + "Z",
            },
            {
                "id": "activity_4",
                "type": "system",
                "description": "Daily safety inspection completed for all zones",
                "timestamp": datetime.utcnow().isoformat() + "Z",
            },
        ],
        "zone_statistics": {
            "Zone A - Deep Excavation": {
                "workers": 3,
                "machinery": 2,
                "incidents": 2,
                "risk_level": "high",
                "safety_score": 65,
            },
            "Zone B - Ventilation Shaft": {
                "workers": 2,
                "machinery": 2,
                "incidents": 2,
                "risk_level": "medium",
                "safety_score": 75,
            },
            "Zone C - Mineral Processing": {
                "workers": 1,
                "machinery": 1,
                "incidents": 1,
                "risk_level": "medium",
                "safety_score": 80,
            },
            "Zone D - Exploration Tunnel": {
                "workers": 2,
                "machinery": 1,
                "incidents": 1,
                "risk_level": "low",
                "safety_score": 88,
            },
        },
        "performance_trends": {
            "last_7_days": {
                "incidents": [2, 1, 3, 2, 1, 4, 2],
                "equipment_failures": [0, 1, 0, 0, 1, 0, 1],
                "worker_health_issues": [1, 0, 2, 1, 0, 1, 2],
                "safety_score": [82, 85, 78, 81, 84, 76, 78],
            }
        },
        "metadata": {
            "last_updated": datetime.utcnow().isoformat() + "Z",
            "data_version": "1.0.0",
            "mine_name": "MiningMitra Demo Site",
            "location": "India - Mining Region",
        }
    }


@router.get("/alerts/live")
def get_live_alerts():
    """Get real-time alerts for demo"""
    return {
        "critical_alerts": [
            {
                "id": "crit_1",
                "title": "Critical Health Alert",
                "description": "Worker Vikram Singh - Heart rate 120 BPM, Oxygen level 88%",
                "zone": "Zone A - Deep Excavation",
                "severity": "critical",
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "action_required": "Immediate medical attention required",
            },
            {
                "id": "crit_2",
                "title": "Structural Failure Risk",
                "description": "Support beam cracks detected - Collapse risk imminent",
                "zone": "Zone C - Mineral Processing",
                "severity": "critical",
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "action_required": "Evacuate zone immediately",
            },
        ],
        "warnings": [
            {
                "id": "warn_1",
                "title": "Equipment Maintenance Alert",
                "description": "Rotary Drill RD-2500 vibration levels exceeding safe limits",
                "zone": "Zone D - Exploration Tunnel",
                "severity": "warning",
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "action_required": "Schedule immediate maintenance",
            },
            {
                "id": "warn_2",
                "title": "Worker Fatigue Alert",
                "description": "Mohammed Ali showing signs of high fatigue",
                "zone": "Zone B - Ventilation Shaft",
                "severity": "warning",
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "action_required": "Recommend rest break",
            },
        ],
        "total_alerts": 4,
        "critical_count": 2,
        "warning_count": 2,
    }
