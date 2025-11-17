# 🏭 MiningMitra Backend API - Demo Documentation

## 🎯 Project Overview

**MiningMitra** is a comprehensive Mining Safety & Monitoring System that provides real-time tracking of workers, equipment, incidents, and environmental conditions in mining operations.

### ✨ Key Features

- 👷 **Worker Health Monitoring** - Real-time vitals tracking (heart rate, oxygen levels, temperature, fatigue)
- 🚜 **Machinery Management** - Equipment health monitoring with predictive maintenance alerts
- ⚠️ **Incident Management** - Real-time incident reporting with severity classification and heatmaps
- 🛣️ **Corridor Monitoring** - Environmental compliance tracking (pollution, temperature, traffic)
- 📊 **Live Dashboard** - Comprehensive statistics and critical alerts
- 🔬 **Pollution Analysis** - Environmental impact calculations
- 🛡️ **Safety Scoring** - Automated safety score calculation based on multiple parameters

---

## 🚀 Quick Start for Demo

### 1. **View Interactive API Documentation**

Open your browser and visit:
- **Swagger UI**: http://localhost:8000/docs (Interactive API testing)
- **ReDoc**: http://localhost:8000/redoc (Beautiful documentation)
- **Root Endpoint**: http://localhost:8000/ (API overview)

### 2. **Test Key Endpoints**

#### 📊 Dashboard Statistics
```bash
curl http://localhost:8000/api/dashboard/statistics
```
Returns comprehensive mining operation statistics including:
- Worker health metrics
- Equipment status
- Active incidents
- Zone-wise breakdowns
- Performance trends
- Live alerts

#### 🚨 Live Alerts
```bash
curl http://localhost:8000/api/dashboard/alerts/live
```
Shows critical alerts and warnings requiring immediate attention.

#### 👷 Workers Monitoring
```bash
# Get all workers
curl http://localhost:8000/api/workers

# Get critical workers only
curl http://localhost:8000/api/workers/critical
```

#### 🚜 Machinery Status
```bash
# Get all machinery
curl http://localhost:8000/api/machinery

# Get machinery requiring maintenance
curl http://localhost:8000/api/machinery/critical
```

#### ⚠️ Incidents
```bash
# Get all incidents
curl http://localhost:8000/api/incidents

# Get active incidents
curl http://localhost:8000/api/incidents/active

# Get incident heatmap
curl http://localhost:8000/api/incidents/heatmap
```

#### 🛣️ Corridors
```bash
# Get all corridors
curl http://localhost:8000/api/corridors

# Get average metrics
curl http://localhost:8000/api/corridors/metrics/average
```

#### 🔬 Analytics
```bash
# Calculate pollution index
curl "http://localhost:8000/api/pollution?depth=100&explosives=50"

# Calculate safety score
curl "http://localhost:8000/api/safety?temperature=30&vibration=5"
```

---

## 📊 Demo Data Summary

### Workers: 8 Total
- 6 Active workers
- 1 Critical status (Vikram Singh - High heart rate & low oxygen)
- 1 Warning status (Mohammed Ali - High fatigue)
- Diverse roles: Miners, Engineers, Supervisors, Operators, Technicians, Geologist

### Machinery: 6 Units
- 5 Operational
- 1 Requiring Maintenance (Rotary Drill RD-2500)
- Types: Excavator, Drill, Loader, Haul Truck, Continuous Miner, Ventilation System

### Incidents: 6 Total
- 4 Active incidents
- 2 Resolved
- Severity levels: Critical, High, Medium
- Types: Gas Leak, Equipment Failure, Structural Issues, Health Emergencies

### Zones: 4 Monitoring Areas
- Zone A - Deep Excavation (High Risk)
- Zone B - Ventilation Shaft (Medium Risk)
- Zone C - Mineral Processing (Medium Risk)
- Zone D - Exploration Tunnel (Low Risk)

---

## 🎨 Demo Presentation Tips

### For Judges:

1. **Start with Dashboard** (`/api/dashboard/statistics`)
   - Shows comprehensive overview of entire mining operation
   - Highlights real-time metrics and KPIs
   - Demonstrates data-driven decision making

2. **Show Live Alerts** (`/api/dashboard/alerts/live`)
   - Critical health alerts for workers
   - Equipment maintenance warnings
   - Structural safety concerns
   - Demonstrates proactive monitoring

3. **Worker Safety Focus** (`/api/workers`, `/api/workers/critical`)
   - Real-time health vitals tracking
   - Location-based monitoring
   - Fatigue level assessment
   - Critical worker identification

4. **Equipment Intelligence** (`/api/machinery`, `/api/machinery/critical`)
   - Predictive maintenance alerts
   - Operating hours tracking
   - Efficiency metrics
   - Vibration and temperature monitoring

5. **Incident Management** (`/api/incidents/heatmap`)
   - Zone-wise incident visualization
   - Severity classification
   - Affected workers tracking
   - Historical incident data

6. **Interactive Documentation** (`/docs`)
   - Try out any endpoint directly
   - See request/response schemas
   - Test with different parameters

---

## 🌐 Deployment to Render.com

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Add complete demo endpoints with dashboard and analytics"
git push origin main
```

### Step 2: Render.com will auto-deploy
- Wait 2-5 minutes for deployment
- Check logs in Render.com dashboard
- Verify deployment success

### Step 3: Set Environment Variables
In Render.com dashboard, add:
```
NODE_ENV=production
FRONTEND_URL=https://miningmitra.vercel.app
```

### Step 4: Test Live Endpoints
```bash
# Test health check
curl https://backend-b3ru.onrender.com/health

# Test dashboard
curl https://backend-b3ru.onrender.com/api/dashboard/statistics

# Test workers
curl https://backend-b3ru.onrender.com/api/workers
```

### Step 5: View Live Documentation
Visit: https://backend-b3ru.onrender.com/docs

---

## 📋 API Endpoints Summary

| Category | Endpoint | Method | Description |
|----------|----------|--------|-------------|
| **Dashboard** | `/api/dashboard/statistics` | GET | Complete operation statistics |
| | `/api/dashboard/alerts/live` | GET | Real-time critical alerts |
| **Workers** | `/api/workers` | GET | All workers |
| | `/api/workers/critical` | GET | Critical health workers |
| | `/api/workers/{id}` | GET | Specific worker details |
| | `/api/workers` | POST | Add new worker |
| | `/api/workers/{id}` | PUT | Update worker |
| | `/api/workers/{id}` | DELETE | Remove worker |
| **Machinery** | `/api/machinery` | GET | All machinery |
| | `/api/machinery/critical` | GET | Maintenance required |
| | `/api/machinery/{id}` | GET | Specific machinery |
| | `/api/machinery` | POST | Add machinery |
| | `/api/machinery/{id}` | PUT | Update machinery |
| | `/api/machinery/{id}` | DELETE | Remove machinery |
| **Incidents** | `/api/incidents` | GET | All incidents |
| | `/api/incidents/active` | GET | Active incidents only |
| | `/api/incidents/critical` | GET | Critical incidents |
| | `/api/incidents/heatmap` | GET | Zone-wise heatmap |
| | `/api/incidents/{id}` | GET | Specific incident |
| | `/api/incidents` | POST | Report incident |
| | `/api/incidents/{id}` | PUT | Update incident |
| | `/api/incidents/{id}` | DELETE | Remove incident |
| **Corridors** | `/api/corridors` | GET | All corridors |
| | `/api/corridors/metrics/average` | GET | Average metrics |
| | `/api/corridors/{id}` | GET | Specific corridor |
| | `/api/corridors` | POST | Add corridor |
| | `/api/corridors/{id}` | PUT | Update corridor |
| | `/api/corridors/{id}` | DELETE | Remove corridor |
| **Analytics** | `/api/pollution` | GET | Pollution index calculation |
| | `/api/safety` | GET | Safety score calculation |
| **System** | `/` | GET | API overview |
| | `/health` | GET | Health check |
| | `/docs` | GET | Interactive documentation |
| | `/redoc` | GET | Alternative documentation |

---

## 🔧 Technology Stack

- **Framework**: FastAPI (Python)
- **CORS**: Configured for frontend integration
- **Documentation**: Auto-generated Swagger/OpenAPI
- **Deployment**: Render.com
- **Data Models**: Pydantic for validation

---

## 🎯 Unique Selling Points for Demo

1. ✅ **Real-time Monitoring** - Live worker vitals and equipment status
2. ✅ **Predictive Analytics** - Equipment failure prediction
3. ✅ **Comprehensive Dashboard** - Single view of entire operation
4. ✅ **Intelligent Alerts** - Priority-based notification system
5. ✅ **Zone-based Tracking** - Location-aware monitoring
6. ✅ **Environmental Compliance** - Pollution and safety metrics
7. ✅ **Interactive Documentation** - Easy API exploration
8. ✅ **RESTful Design** - Standard, scalable architecture

---

## 📞 Support

For questions or issues during the demo:
- Check `/docs` for interactive testing
- Verify server is running: `/health` endpoint
- Review `/` endpoint for API structure overview

---

## 🏆 Ready for Demo!

Your backend is now production-ready with:
- ✅ 8 Workers with realistic Indian names and roles
- ✅ 6 Machinery units with detailed specifications
- ✅ 6 Incidents across multiple severity levels
- ✅ 5 Corridors with environmental metrics
- ✅ Comprehensive dashboard with statistics
- ✅ Live alerts system
- ✅ Interactive API documentation
- ✅ CORS configured for frontend
- ✅ Health monitoring endpoints

**Go impress that judge! 🚀**
