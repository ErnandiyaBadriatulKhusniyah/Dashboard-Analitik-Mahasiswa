import { useState, useEffect } from "react";
import HeaderDashboard from "../components/molecules/HeaderDashboard";
import Layout from "../components/templates/Layout";
import Data from "../data/mahasiswaAktif.json";

const MahasiswaAktif = () => {
    const [searchNim, setSearchNim] = useState("");
    const [currentPage, setCurrentPage] = useState(1);
    const itemsPerPage = 10;

    const getStatusStyle = (status) => {
        switch (status) {
            case "Lulus Tepat Waktu":
                return "text-blue-500 border border-blue-500 px-3 py-1 rounded";
            case "Terlambat Lulus":
                return "text-yellow-500 border border-yellow-500 px-3 py-1 rounded";
            default:
                return "";
        }
    };

    const filteredData = Data.filter((mhs) =>
        mhs.nim.toLowerCase().includes(searchNim.toLowerCase())
    );

    const totalPages = Math.ceil(filteredData.length / itemsPerPage);
    const paginatedData = filteredData.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage);

    return (
        <main className="h-screen w-full ">
            <Layout className="flex flex-col gap-10">
                <HeaderDashboard children="Mahasiswa > Mahasiswa Aktif" />
                <div className="flex justify-end px-3 mt-3 ">
                    <input
                        type="text"
                        placeholder="Cari mahasiswa dengan NIM"
                        className="border px-10 py-1 rounded shadow bg-white"
                        value={searchNim}
                        onChange={(e) => setSearchNim(e.target.value)} />
                </div>
                <div className="overflow-x-auto rounded-xl shadow-lg p-4 bg-white flex gap-10 justify-center my-5 ">
                    <table className="min-w-full table-auto border-collapse">
                        <thead className="bg-gray-200 text-gray-700">
                            <tr>
                                <th className="px-6 py-3 text-left">Nama</th>
                                <th className="px-6 py-3 text-left">Angkatan</th>
                                <th className="px-6 py-3 text-left">NIM</th>
                                <th className="px-6 py-3 text-left">Status Studi</th>
                                <th className="px-6 py-3 text-left">Detail</th>
                            </tr>
                        </thead>
                        <tbody>

                            {paginatedData.map((mhs, i) => (
                                <tr key={i} className="border-b hover:bg-gray-50">

                                </tr>
                            ))}



                        </tbody>

                    </table>

                </div>


            </Layout>

        </main >
    )
};




export default MahasiswaAktif;