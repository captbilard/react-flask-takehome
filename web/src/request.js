import axios from "axios";

const url = "http://127.0.0.1:3001";

export async function getAllCompanies() {
  try {
    let value = await axios({
      method: "get",
      url: `${url}/companies`,
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
    });
    return value.data.resource;
  } catch (error) {
    console.log("error", error);
  }
}

export async function getCleanersInCompany(company_id) {
  try {
    let value = await axios({
      method: "get",
      url: `${url}/users/${company_id}`,
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
    });
    return value.data.resource;
  } catch (error) {
    console.log("error", error);
  }
}

export async function scheduleShift(formData) {
  console.log(formData);
  try {
    // let value = await axios({
    //   method: "post",
    //   url: `${url}/schedule`,
    //   data: formData,
    //   headers: { "Content-Type": "multipart/form-data" },
    // }).catch((error) => console.log(error));
    let value = await axios
      .post(`${url}/schedule`, formData)
      .then((response) => {
        return response;
      })
      .catch((error) => {
        console.log(error);
      });
    return value;
  } catch (error) {
    console.log("error", error);
  }
}
