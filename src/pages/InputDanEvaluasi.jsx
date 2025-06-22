import HeaderDashboard from "../components/molecules/HeaderDashboard";
import Layout from "../components/templates/Layout";

const InputDanEvaluasi = () => {
    return (
        <main className="h-screen w-full">
            <Layout>
                <HeaderDashboard children="Input" />
                <div className="px-6 mt-8 bg-white p-5 rounded-lg shadow-md w-full h-[600px] flex  justify-center">
                    <div className="border px-10 py-1 rounded shadow bg-white w-full h-[70px] flex">

                    </div>
                </div>
            </Layout>
        </main>
    )
}

export default InputDanEvaluasi;