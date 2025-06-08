import Typography from "../atoms/Typograpy";

const HeaderDashboard = ({ children }) => {
    return (
        <div className="flex items-center justify-between bg-white p-4 rounded-lg">
            <Typography variantClass="h1" className="font-semibold">
                {children}
            </Typography>
            <Typography>Hi, Miftahul Rizqha</Typography>
        </div>
    )
}

export default HeaderDashboard;