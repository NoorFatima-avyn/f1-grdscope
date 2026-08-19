# API Documentation

Base URL: https://noorfatimaavyn.pythonanywhere.com/api

## Seasons
GET /api/seasons/{year}/drivers
GET /api/seasons/{year}/races
GET /api/seasons/{year}/driver-standings
GET /api/seasons/{year}/constructor-standings
GET /api/seasons/{year}/headshots

## Races
GET /api/races/{year}/results
GET /api/races/{year}/{round}/podium
GET /api/races/{year}/{round}/winner
GET /api/races/circuit/{circuit_id}/winners
GET /api/races/circuit/{circuit_id}/detail
GET /api/races/circuit/{circuit_id}/image

## Teams
GET /api/teams/car-images/{year}

## AI Chat
POST /api/chat/ask
Body: { "message": "your question" }

## AI Predictions
GET /api/predictions/race/{year}/{round}

## Supported Years
2021, 2022, 2023, 2024, 2025, 2026