'use client'

import Image from "next/image";
import Link from 'next/link';
import { useState } from 'react';



export default function Home() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const handleOnSubmit = async (e: { preventDefault: () => void; }) => {
      e.preventDefault();
      let result = await fetch(
      'http://localhost:3000/', {
          method: "post",
          body: JSON.stringify({ name, email }),
          headers: {
              'Content-Type': 'application/ json'
          }
      })
      if (result.ok) {
        alert("Data saved successfully");
        setEmail("");
        setName("");
      } else {
        console.warn(result);
      }
  }

  return (
    <>
      <h1>This is React WebApp </h1>
      <form action="">
        <input type="text" placeholder="name"
          value={name} onChange={(e) => setName(e.target.value)} />
        <input type="email" placeholder="email"
          value={email} onChange={(e) => setEmail(e.target.value)} />
        <button type="submit"
          onClick={handleOnSubmit}>submit</button>
      </form>

    </>
  );
}
