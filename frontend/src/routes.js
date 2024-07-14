import App from "./App";
import Swimmerslogin from "./components/swimmers-reg";
import Coacheslogin from "./components/coaches-reg";
import Swimmersplash from "./components/summersplash";
import Swimathon from "./components/swimathon";
import Competitiveswimee from "./components/competitiveswimee";
const routes = [
    {
        path: "/",
        element: <App/>,
    },
    {
        path: "/swimmerslogin",
        element:<Swimmerslogin/>,
    },
    {
        path: "/Coacheslogin",
        element:<Coacheslogin/>,
    },
    {
        path: "/summersplash",
        element:<Swimmersplash/>
    },
    {
        path: "/swimathon",
        element:<Swimathon/>
    },
    {
        path: "/competitiveswimee",
        element: <Competitiveswimee/>
    }

   
]
export default routes;