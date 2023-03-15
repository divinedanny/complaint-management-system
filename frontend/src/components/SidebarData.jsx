import React from "react";
import * as FaIcons from "react-icons/fa";
import * as AiIcons from "react-icons/ai";
import * as IoIcons from "react-icons/io";
import * as RiIcons from "react-icons/ri";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Dashboard from "../student/Dashboard";

export const SidebarData = [
{
	title: "Dashboard",
	path:"/dashboard",
	icon: <AiIcons.AiFillHome />,
	iconClosed: <RiIcons.RiArrowDownSFill />,
	iconOpened: <RiIcons.RiArrowUpSFill />
},
{
	title: "Profile",
	path: "/account-Setting",
	icon: <IoIcons.IoIosPaper />,
	iconClosed: <RiIcons.RiArrowDownSFill />,
	iconOpened: <RiIcons.RiArrowUpSFill />,

	subNav: [
	{
		title: "Change Password",
		path: "/account-Setting/password",
		icon: <IoIcons.IoIosPaper />,
		cName: "sub-nav",
	},
	],
},
{
	title: "Add Complaints",
	path: "/complaints/add",
	icon: <FaIcons.FaEnvelopeOpenText />,

	iconClosed: <RiIcons.RiArrowDownSFill />,
	iconOpened: <RiIcons.RiArrowUpSFill />,

	subNav: [
	{
		title: "Complaint History",
		path: "/complaints/history",
		icon: <IoIcons.IoIosPaper />,
	},
	],
},
];
