import * as React from "react";
import "./App.css";
import * as request from "./request";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

function App() {
  const [companies, setCompanies] = React.useState();
  const [cleaners, setCleaners] = React.useState([]);
  const [status, setStatus] = React.useState();

  const handleCleanerList = (event) => {
    request.getCleanersInCompany(event.target.value).then((result) => {
      setCleaners(result);
    });
  };

  const handleStatus = (event) => {
    const selectedCleaner = cleaners.find(
      (cleaner) => cleaner.id === +event.target.value
    );
    setStatus(selectedCleaner.availability_status);
  };

  const notify = () => {
    return toast("Booking was successfully created", {
      position: "top-center",
      autoClose: 5000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const fields = Array.from(
      event.target.querySelectorAll(".form-control")
    ).reduce((acc, field) => ({ ...acc, [field.name]: field.value }), {});
    let formData = { ...fields };
    request
      .scheduleShift(formData)
      .then((response) => {
        notify();
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
      });
    event.target.reset();
  };

  React.useEffect(() => {
    // Update the document title using the browser API
    async function fetchData() {
      const result = await request.getAllCompanies();
      setCompanies(result);
    }
    fetchData();
  }, []);

  return (
    <div className="w-6/12 mx-auto bg-gray-200 rounded-xl shadow border p-8 m-10">
      <h1 className="text-3xl text-gray-700 font-bold mb-5">
        Request a cleaner
      </h1>
      <div className="block p-6 rounded-lg shadow-lg bg-white w-full">
        <form onSubmit={handleSubmit}>
          <div className="grid grid-cols-2 gap-4">
            <div className="form-group mb-6">
              <input
                type="text"
                className="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                id="exampleInput123"
                aria-describedby="emailHelp123"
                placeholder="Client Email Address"
                name="client_email"
              />
            </div>
            <div className="form-group mb-6">
              <select
                className="form-control
                                      block
                                      w-full
                                      px-3
                                      py-1.5
                                      text-base
                                      font-normal
                                      text-gray-700
                                      bg-white bg-clip-padding
                                      border border-solid border-gray-300
                                      rounded
                                      transition
                                      ease-in-out
                                      m-0
                                      focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                id="exampleInput124"
                aria-describedby="emailHelp124"
                placeholder="Select Company"
                name="company"
                onChange={handleCleanerList}
              >
                {companies ? (
                  companies.map(({ id, name }) => (
                    <option key={id} value={id}>
                      {name}
                    </option>
                  ))
                ) : (
                  <option disabled={true}>Select Company</option>
                )}
              </select>
            </div>
          </div>
          <div className="form-group mb-6">
            <select
              className="form-control block
                                w-full
                                px-3
                                py-1.5
                                text-base
                                font-normal
                                text-gray-700
                                bg-white bg-clip-padding
                                border border-solid border-gray-300
                                rounded
                                transition
                                ease-in-out
                                m-0
                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
              id="exampleInput125"
              onChange={handleStatus}
              onClick={handleStatus}
              name="user"
            >
              <option disabled={true} value={""}>
                {" "}
                Select cleaner{" "}
              </option>
              {cleaners
                ? cleaners.map(
                    ({ id, name, email_address, availability_status }) => (
                      <option key={id} value={id}>
                        {name}: {email_address}
                      </option>
                    )
                  )
                : ""}
            </select>
          </div>
          <div className="form-group mb-6">
            <div className="flex justify-between border-b">
              {status ? (
                <h4 className="font-bold">Status: {status}</h4>
              ) : (
                <h4 className="font-bold">...</h4>
              )}
            </div>
            <div className="py-3">
              Select Date
              <input
                type="date"
                className="form-control block
                                    w-full
                                    px-3
                                    py-1.5
                                    text-base
                                    font-normal
                                    text-gray-700
                                    bg-white bg-clip-padding
                                    border border-solid border-gray-300
                                    rounded
                                    transition
                                    ease-in-out
                                    m-0
                                    focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                placeholder="Select Date"
                name="date"
              />
            </div>
            <div className="grid grid-cols-2 gap-4 pt-3">
              <div className="text-sm">Start Hours</div>
              <div className="text-sm">End Hours</div>
              <div className="">
                <input
                  type="time"
                  className="form-control block
                                        w-full
                                        px-3
                                        py-1.5
                                        text-base
                                        font-normal
                                        text-gray-700
                                        bg-white bg-clip-padding
                                        border border-solid border-gray-300
                                        rounded
                                        transition
                                        ease-in-out
                                        m-0
                                        focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                  placeholder="Select"
                  name="start_time"
                />
              </div>
              <div className="">
                <input
                  type="time"
                  className="form-control block
                                        w-full
                                        px-3
                                        py-1.5
                                        text-base
                                        font-normal
                                        text-gray-700
                                        bg-white bg-clip-padding
                                        border border-solid border-gray-300
                                        rounded
                                        transition
                                        ease-in-out
                                        m-0
                                        focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                  placeholder="Select"
                  name="end_time"
                />
              </div>
            </div>
          </div>
          {/*TODO: Handle submit button*/}
          <button
            disabled={status === "Not available"}
            type="submit"
            className="
                w-full
                px-6
                py-2.5
                bg-blue-600
                text-white
                font-medium
                text-xs
                leading-tight
                uppercase
                rounded
                shadow-md
                hover:bg-blue-700 hover:shadow-lg
                focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0
                active:bg-blue-800 active:shadow-lg
                transition
                duration-150
                ease-in-out"
          >
            Book Cleaner
          </button>
        </form>
      </div>
      <ToastContainer />
    </div>
  );
}

export default App;
