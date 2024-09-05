import { useState, useEffect } from "react";
import ProductionCard from "./production/ProductionCard";

function Home() {

	// create state to hold data returned by fetch request
	// we need this because we don't know when our fetch request will resolve
	const [longestMovies, setLongestMovies] = useState([])

	useEffect(() => {
		// this is how we communicate with flask
		// by making fetch requests
		fetch("http://127.0.0.1:5555/longest-movies")
		.then(res => {
			if(res.ok) {
				return res.json()
			} else {
				console.error("fetch http://127.0.0.1:5555/longest-movies went wrong")
			}
		})
		.then(data => setLongestMovies(data))
	}, []) // don't forget the empty dependency array

	return (
		<div>
			<section>
				<h2>Longest Movies</h2>
			</section>
			<ul
				style={{
					display: "flex",
					flexWrap: "wrap",
					justifyContent: "center",
				}}
			>
				{longestMovies.map((el) => (
					<section style={{ display: "flex", flexDirection: "column" }}>
						<h3>{el.length} minutes</h3>

						<ProductionCard key={el.id} production={el} />
					</section>
				))}
			</ul>

			<section>
				<h2>Most Popular Actors</h2>
			</section>
		</div>
	);
}

export default Home;
