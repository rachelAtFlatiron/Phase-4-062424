import { redirect, useNavigate } from "react-router-dom";
import { useFormik } from "formik";
import * as yup from "yup";

function ProductionForm() {

	//1. create yup schema
	//2. use useFormik hook to set schema, initialValues, onSubmit
	//3. onSubmit POST request
	//4. hook up useFormik to JSX espeically the onSubmit, values, onChange, errors (opt)
	const navigate = useNavigate()
	
	//1. create schema for the values for form 
	const schema = yup.object().shape({
		title: yup.string().required("required"),
		genre: yup.string(),
		length: yup.number().positive("must be greater than 0"),
		year: yup.number().min(1850, "movies didn't become a thing until 1850 maybe"),
		image: yup.string().required("required"),
		language: yup.string(),
		director: yup.string(),
		description: yup.string().max(50, "must be less than 50 characters"),
		composer: yup.string()
	})

	//2. create use formik hook
	const formik = useFormik({
		//set initial values
		initialValues: {
			title: 'Pacific Rim 2',
			genre: 'Action',
			length: 120,
			year: 2013,
			image: 'sadf.png',
			language: 'English',
			director: 'Guillermo del Toro',
			description: 'Boom Boom',
			composer: 'idk'
		},
		//set schema
		validationSchema: schema,
		//3. create onSubmit callback
		//if your page is refreshing make sure you added onSubmit handler to JSX
		onSubmit: (values) => {
			console.log(formik.errors)
			//POST request
			fetch("http://127.0.0.1:5555/productions", {
				method: "POST",
				body: JSON.stringify(values),
				headers: {'content-type': 'application/json'}
			})
			.then(res => {
				if(res.ok){
					return res.json()
				} else {
					console.error("something went wrong with POST productions")
				}
			})
			.then(data => {
				console.log(`/productions/${data.id}`)
				//maybe update parent state and use inverse flow to pass up new production
				
				navigate(`/productions/${data.id}`)
			})

		}
	})
		


	return (
		<section>
			{/* 4. hook up formik submit, onchange, values, and errors */}
			<form onSubmit={formik.handleSubmit} className="form" >
				<label>Title </label>
				<input
					type="text"
					name="title"
					onChange={formik.handleChange}
					value={formik.values.title}
				/>
				{formik.errors.title && formik.touched.title ? (<h3 style={{ color: "red" }}>{formik.errors.title}</h3>) : "" }


				<label> Genre</label>
				<input
					type="text"
					name="genre"
					onChange={formik.handleChange}
					value={formik.values.genre}
				/>
				{formik.errors.genre && formik.touched.genre ? (<h3 style={{ color: "red" }}>{formik.errors.genre}</h3>) : "" }

				<label>Length</label>
				<input
					type="number"
					name="length"
					onChange={formik.handleChange}
					value={formik.values.length}
					
				/>
				{formik.errors.length && formik.touched.length ? (<h3 style={{ color: "red" }}>{formik.errors.length}</h3>) : "" }
				

				<label>Year</label>
				<input
					type="number"
					name="year"
					onChange={formik.handleChange}
					value={formik.values.year}
					
				/>
				{formik.errors.year && formik.touched.year ? (<h3 style={{ color: "red" }}>{formik.errors.year}</h3>) : "" }
				<label>Image</label>
				<input
					type="text"
					name="image"
					onChange={formik.handleChange}
					value={formik.values.image}
					
				/>
				
				<label>Language</label>
				<input
					type="text"
					name="language"
					onChange={formik.handleChange}
					value={formik.values.language}
					
				/>
				{formik.errors.language && formik.touched.language ? (<h3 style={{ color: "red" }}>{formik.errors.language}</h3>) : "" }

				<label>Director</label>
				<input
					type="text"
					name="director"
					onChange={formik.handleChange}
					value={formik.values.director}
					
				/>
				{formik.errors.director && formik.touched.director ? (<h3 style={{ color: "red" }}>{formik.errors.director}</h3>) : "" }

				<label>Description</label>
				<textarea
					type="text"
					rows="4"
					cols="50"
					name="description"
					onChange={formik.handleChange}
					value={formik.values.description}
					
				/>
				{formik.errors.description && formik.touched.description ? (<h3 style={{ color: "red" }}>{formik.errors.description}</h3>) : "" }
				
				<label>Composer</label>
				<input
					type="text"
					name="composer"
					onChange={formik.handleChange}
					value={formik.values.composer}
					
				/>
				{formik.errors.composer && formik.touched.composer ? (<h3 style={{ color: "red" }}>{formik.errors.composer}</h3>) : "" }

				<input className="button" type="submit" />
			</form>
		</section>
	);
}

export default ProductionForm;
