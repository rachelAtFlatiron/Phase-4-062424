import { Routes, Route } from "react-router-dom";
import { useEffect, useState } from "react";
import Home from "./components/Home";
import Navigation from "./components/Navigation";
import NotFound from "./components/NotFound";
import ActorForm from "./components/actor/ActorForm";
import ActorContainer from "./components/actor/ActorContainer";
import ActorDetail from "./components/actor/ActorDetail";
import ProductionContainer from "./components/production/ProductionContainer";
import ProductionForm from "./components/production/ProductionForm";
import ProductionDetail from "./components/production/ProductionDetail";
import Auth from "./components/Auth";

function App() {
	const [productions, setProductions] = useState([]);
	const [actors, setActors] = useState([]);
	// ✅ 4. Pass the new user to App.js
	// ✅ 4a. create user state and update user function
	const [user, setUser] = useState(null)

	useEffect(() => {
		fetch("/productions")
			.then((res) => res.json())
			.then(setProductions);
		fetch("/actors")
			.then((res) => res.json())
			.then(setActors);
		// ✅ 9a. fetch GETs `/authenticate-session` in `useEffect`
		fetch('/authenticate-session')
		.then(res => {
			// ✅ 9b. if res.ok update user with the response
			if(res.ok){
				res.json().then(data => {
					setUser(data)
				})
			} else {
				setUser(null)
			}
		})
	}, []);

	// ✅ 4a. update user function
	const updateUser = (user) => {
		setUser(user)
	}

	const addProduction = (production) =>
		setProductions((current) => [...current, production]);
	
	// ✅ 7a. if no user, return essential JSX
	if (!user){
		return (
			<div className="App light">
				<Navigation updateUser={updateUser} user={user} />
				<Auth updateUser={updateUser} />
			</div>
		)
	}
	// ✅ 11. Show user greeting in `Navigation.js`
	// ✅ 11a. pass down user as props
	// ✅ 11b. Conditionally render the logout button and a greeting
	return (
		<div className="App light">
			
			<Navigation updateUser={updateUser} user={user} />
			<Routes>
				< Route path = "/auth" element={<Auth updateUser={updateUser} />} />

				<Route path="/actors/new" element={<ActorForm />} />

				<Route path="/productions/new" element={<ProductionForm addProduction={addProduction} />} />
				
				<Route path="/productions/:id" element={<ProductionDetail />} />

				<Route path="/productions" element={<ProductionContainer productions={productions} />} />

				<Route path="/actors/:id" element={<ActorDetail />} />

				<Route path="/actors" element={<ActorContainer actors={actors} />} />

				<Route path="/not-found" element={<NotFound />} />

				<Route exact path="/" element={<Home />} />
			</Routes>
		</div>
	);
}

export default App;
