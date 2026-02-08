"use client"

import React, { use, useEffect } from "react";
import api from "./api";
import toast from "react-hot-toast";

type Transaction = {
  id: number;
  text: string;
  amount: number;
  created_at: string;
}

export default function Home() {
  const [transactions, setTransactions] = React.useState<Transaction[]>([]);

  const getTransactions = async () => {
    try {
      const res = await api.get<Transaction[]>("transactions/");
      setTransactions(res.data);
      toast.success("Transactions loaded");
    } catch (err) {
      console.error(err);
      toast.error("Failed to load transactions");
    }
  }
  useEffect(() => {
    getTransactions();
  }, []);
  return (
    <button className="btn btn-small">
      test
    </button>
  );
}
