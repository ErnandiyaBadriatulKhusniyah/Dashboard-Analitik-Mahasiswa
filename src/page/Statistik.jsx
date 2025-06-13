import HeaderDashboard from "../components/molecules/HeaderDashboard";
import Layout from "../components/templates/Layout";
import { ArrowDownToLine } from 'lucide-react';

const Statistik = () => {
    return(
        <main className="h-screen w-full">
            <Layout>
                <HeaderDashboard children="Statistik"/>
                 <div className="px-6 mt-8 bg-white p-5 rounded-lg shadow-md w-full h-[600px] flex  justify-center">
                    <button className="w-full h-[600px] bg-gray-300 p-5 rounded-lg">Tambahkan File</button>

                 </div>
            </Layout>

        </main>
    )

}

export default Statistik;