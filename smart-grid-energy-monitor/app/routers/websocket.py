from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter(tags=["WebSocket"])

# Store all connected dashboard clients
connected_clients = []


# ================= Broadcast Function =================

async def broadcast_alert(message: str):

    disconnected_clients = []

    for client in connected_clients:

        try:
            await client.send_text(message)

        except Exception:
            disconnected_clients.append(client)

    # Remove disconnected clients
    for client in disconnected_clients:

        if client in connected_clients:
            connected_clients.remove(client)


# ================= WebSocket Endpoint =================

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    connected_clients.append(websocket)

    print("🟢 Client Connected")

    try:

        while True:

            message = await websocket.receive_text()

            print("Received:", message)

            # Broadcast message to all connected dashboards
            await broadcast_alert("🟢 Dashboard updated successfully")

    except WebSocketDisconnect:

        if websocket in connected_clients:
            connected_clients.remove(websocket)

        print("🔴 Client Disconnected")