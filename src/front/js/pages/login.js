import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";

export const Login = () => {
	const { store, actions } = useContext(Context);
	const [user, setUser] = useState('');
	const [password, setPassword] = useState('');

	const token = sessionStorage.getItem("token");
	console.log("This is your token", store.token);
	const handleClick = () => {
		actions.login(user, password);
	};

	if (store.token && store.token != "" && store.token != undefined);




	return (
		<div className="text-center mt-5">
			<h1>Login</h1>
			{token && token != "" && token != undefined ? ("You are logged in with this token" + token)
			: (
			<div>
				Username:
				<input type="text" placeholder="username.." onChange={(e) => setUser(e.target.value)} value={user}></input>
				Password:
				<input type="password" placeholder="password.." onChange={(e) => setPassword(e.target.value)} value={password}></input>
				<button onClick={(handleClick)}>Login</button>
			</div>
				)}
		</div>
	);
};