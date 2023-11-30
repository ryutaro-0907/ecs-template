// pages/index.js
import React from "react";

const HomePage = ({ data }) => {
  return (
    <div>
      <h1>Next.js with Backend API</h1>
      <p>Data from API: {data.message}</p>
    </div>
  );
};

export async function getStaticProps() {
  // Fetch data from your backend API
  const response = await fetch("http://backend:8000/api/hello");
  const data = await response.json();

  return {
    props: {
      data,
    },
    revalidate: 60, // Set the revalidation period in seconds
  };
}

export default HomePage;
