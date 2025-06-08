
import HeaderDashboard from "../components/molecules/HeaderDashboard";
import Layout from "../components/templates/Layout";

const Mahasiswa = () => {


    return (
        <main className="h-screen w-full">
            <Layout>
                <HeaderDashboard children="Mahasiswa" />
            </Layout>   
        </main>
    );
};

export default Mahasiswa;
