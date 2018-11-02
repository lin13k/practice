# Implement the class below, keeping the constructor's signature unchanged; it should take no arguments.
from collections import defaultdict
import json


class MarkingPositionMonitor:
    def __init__(self):
        self._approvedOrderSet = set()
        self._positions = defaultdict(lambda: 0)
        self._orders = {}

    def on_event(self, message):
        mObj = json.loads(message)
        t = mObj["type"]
        if t == "NEW":
            self.new_order_handler(mObj)
            order = mObj
        else:
            order = self._orders[mObj["order_id"]]
            if t == "ORDER_ACK":
                self.order_ack_handler(mObj, order)
            elif t == "ORDER_REJECT":
                self.order_reject_handler(mObj, order)
            elif t == "CANCEL":
                self.cancel_handler(mObj, order)
            elif t == "CANCEL_ACK":
                self.cancel_ack_handler(mObj, order)
            elif t == "CANCEL_REJECT":
                self.cancel_reject_handler(mObj, order)
            elif t == "FILL":
                self.fill_handler(mObj, order)
        return self._positions[order["symbol"]]

    def new_order_handler(self, obj):
        if obj["side"] == "SELL":
            self._positions[obj["symbol"]] -= obj["quantity"]
        self._orders[obj["order_id"]] = obj

    def order_ack_handler(self, obj, order):
        pass

    def order_reject_handler(self, obj, order):
        if order["side"] == "SELL":
            self._positions[order["symbol"]] += order["quantity"]

    def cancel_handler(self, obj, order):
        pass

    def cancel_ack_handler(self, obj, order):
        if order["side"] == "SELL":
            self._positions[
                order["symbol"]] += order.get(
                    "remaining_quantity", order["quantity"])

    def cancel_reject_handler(self, obj, order):
        pass

    def fill_handler(self, obj, order):
        order["remaining_quantity"] = obj["remaining_quantity"]
        if order["side"] == "SELL":
            pass
        else:
            self._positions[order["symbol"]] += obj["filled_quantity"]
