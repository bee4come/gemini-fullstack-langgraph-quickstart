.PHONY: help dev

help:
	@echo "Available commands:"
	@echo "  make dev  - Starts the backend development server (Uvicorn with reload)"

dev:
	@echo "Starting backend development server..."
	@cd backend && langgraph dev
