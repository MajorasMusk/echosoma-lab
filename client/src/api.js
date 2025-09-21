import axios from "axios";

const API = "https://echosoma-lab.onrender.com/";

export async function runSigil(text) {
  const res = await axios.post(`${API}/sigil?text=${text}`);
  return res.data;
}

export async function getArchive() {
  const res = await axios.get(`${API}/archive`);
  return res.data;
}
