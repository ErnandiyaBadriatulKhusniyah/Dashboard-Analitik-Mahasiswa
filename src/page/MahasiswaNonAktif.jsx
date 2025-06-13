import HeaderDashboard from "../components/molecules/HeaderDashboard";
import Layout from "../components/templates/Layout";
import Data from "../data/mahasiswaNonAktif.json";

const MahasiswaNonAktif = () => {
    const getStatusStyle = (status) => {
        switch (status) {
            case "Cuti": return "text-red-500 border border-red-500 px-10 py-1 rounded";
            case "Keluar": return "text-gray-500 border border-gray-400 px-8 py-1 rounded";
            case "DO": return "text-black border border-black px-10 py-1 rounded font-bold";
            default: return "";
        }
    };

    return (
        <main className="h-screen w-full ">
            <Layout>
                <HeaderDashboard children="Mahasiswa > Mahasiswa Non Aktif" />

                <div className="overflow-x-auto rounded-xl shadow-lg p-4 bg-white flex gap-10 justify-center my-6">
                    <table className="min-w-full table-auto border-collapse">
                        <thead className="bg-gray-200 text-gray-700 ">
                            <tr>
                                <th className="px-6 py-3 text-left">Nama</th>
                                <th className="px-6 py-3 text-left">Angkatan</th>
                                <th className="px-6 py-3 text-left">NIM</th>
                                <th className="px-6 py-3 text-left">Status Studi</th>
                            </tr>
                        </thead>
                        <tbody>
                            {Data.map((mhs, i) => (
                                <tr key={i} className="border-b hover:bg-gray-50">
                                    <td className="px-6 py-3">{mhs.nama}</td>
                                    <td className="px-6 py-3">{mhs.angkatan}</td>
                                    <td className="px-6 py-3">{mhs.nim}</td>
                                    <td className="px-6 py-3">
                                        <span className={getStatusStyle(mhs.status)}>{mhs.status}</span>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </Layout>
        </main>
    );
};





export default MahasiswaNonAktif;