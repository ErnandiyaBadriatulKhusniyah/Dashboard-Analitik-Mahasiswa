
import HeaderDashboard from "../components/molecules/HeaderDashboard";
import Layout from "../components/templates/Layout";
import CardMahasiswa from "../components/molecules/CardMahasiswa";
import IconUser from "../assets/icon/IconUsers.svg";


const Mahasiswa = () => {
    return (
        <main className="h-screen w-full">
            <Layout>
                <HeaderDashboard children="Mahasiswa" />
                <div className="px-6 mt-8">
                    <div className="flex gap-10 justify-center my-6">

                        <CardMahasiswa
                            icon={IconUser}
                            jumlah="85"
                            label="Mahasiswa Aktif"
                            to="/mahasiswaAktif"
                        />
                        <CardMahasiswa
                            icon={IconUser}
                            jumlah="20"
                            label="Mahasiswa Non Aktif"
                            to="/MahasiswaNonAktif"
                        />
                        <CardMahasiswa
                            icon={IconUser}
                            jumlah="105"
                            label="Jumlah Mahasiswa"
                        />
                    </div>

                    <div className="bg-white p-5 rounded-lg shadow-md w-full h-[400px] flex  gap-y-10 justify-center"> Statistik Mahasiswa</div>
                </div>
            </Layout>
        </main>
    );
};

export default Mahasiswa;
