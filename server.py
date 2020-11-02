from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import TextElement
from mesa.visualization.UserParam import UserSettableParameter
from Visualizatons_module.CanvasGridVisualization import CanvasGrid
from Visualizatons_module.ChartVisualization import ChartModule
from Visualizatons_module.TextDisplay import TextDisplay

from model import MainModel, InfectionState, QuarantineState
from agent import MainAgent

clean_color = "#00008b"
recovered_color = "#008000"
quarantine_color = "#FFA500"
infected_color = "#FF0000"
dead_color = "#000000"

# Text elements to Display

class SpaceTextElement(TextElement) :
	def __init__(self) :
		pass

	def render(self, model) :
		return "\n"


class AgentInfectionStatusElement(TextElement) :
	def __init__(self) :
		pass

	def render(self, model) :
		return "Infection State : " + str(model.agent_tracking_infectionstate())


class AgentQuarantineStatusElement(TextElement) :
	def __init__(self) :
		pass

	def render(self, model) :
		return "Quarantine State : " + str(model.agent_tracking_quarantinestate())

class AgentActionTaken(TextElement) :
	def __init__(self) :
		pass

	def render(self, model) :
		return "Action Taken : " + str(model.agent_tracking_action())

class InfectedTextElement(TextElement) :
	def __init__(self) :
		pass

	def render(self, model) :
		infected_number = model.get_infection_number()
		return "Infected Agents : " + str(infected_number)

class RecoveredTextElement(TextElement) :
	def __init__(self) :
		pass

	def render(self, model) :
		recovered_number = model.get_recovered_number()
		return "Recovered Agents : " + str(recovered_number)

class DeadTextElement(TextElement) :
	def __init__(self) :
		pass

	def render(self, model) :
		dead_number = model.get_dead_number()
		return "Dead Agents : " + str(dead_number)

class AgentsLegend(TextElement) :
	def __init__(self) :
		pass

	def render (self, model) :
		return "Agent colors - Susceptible: Blue, Quarantine: Orange, Infected: Red, Recovered: Green"

# Color coding of different states, to improve - add colorcoding to mix of two states. ex : Infected and Quarantine

def draw(agent) :
	if agent is None :
		return

	portrayal = {"Shape" : "circle", "r" : 0.5, "Filled" : "true", "Layer" : 0}

	if agent.infectionstate == InfectionState.CLEAN :		
		portrayal["Color"] = clean_color
	elif agent.infectionstate == InfectionState.RECOVERED :
		portrayal["Color"] = recovered_color #green
	elif agent.quarantinestate == QuarantineState.QUARANTINE :
		portrayal["Color"] = quarantine_color   #orange
	elif agent.infectionstate == InfectionState.INFECTED :
		portrayal["Color"] = infected_color
		

	return portrayal

space_text_element = SpaceTextElement()
infected_number_text_element = InfectedTextElement()
recovered_number_text_element = RecoveredTextElement()
dead_number_text_element = DeadTextElement()
agent_legend_element = AgentsLegend()
canvas_element = CanvasGrid(draw, 40, 40, 400, 400)
agent_infection_status_element = AgentInfectionStatusElement()
agent_quarantine_status_element = AgentQuarantineStatusElement()
agent_action_status_element = AgentActionTaken()

line_chart = ChartModule(
	[
		{"Label" : "Susceptible", "Color": clean_color},
		{"Label" : "Recovered", "Color" : recovered_color},
		{"Label" : "Infected", "Color" : infected_color},
	],canvas_width=20,canvas_height=10,pos_top = 16, pos_left = -550
)

line_chart_aspiration_comparision = ChartModule(
	[	
		{"Label" : "Average Aspiration", "Color" : "#9400D3"},
		{"Label" : "Average Stay In", "Color" : "#FFA500"},
		{"Label" : "Average Get Out", "Color" : "#E033ff"}
	],canvas_width=100,canvas_height=50, pos_top = -350, pos_left = 200

)

model_legend = TextDisplay()

# line_chart_agent = ChartModule(
# 	[
# 		{"Label" : "Aspiration", "Color" : "#9400D3"},
# 		{"Label" : "Stay in probability", "Color" : "#3349FF"},
# 		{"Label" : "Go out probability", "Color" : "#FF3C33"},
# 	]

# )

# Declare model parameters

model_params = {
    "height": 40,
    "width": 40,
    "population_density" : UserSettableParameter("slider", "Population Density", 0.5, 0.1, 0.8, 0.1),
    "death_rate" : 0.02,
    #"transfer_rate" : 0.3,
    "transfer_rate" : UserSettableParameter("slider", "Virus Transfer Rate", 0.3, 0.1, 0.6, 0.1),
    #"initial_infection_rate" : 0.02,
    "initial_infection_rate" : UserSettableParameter("slider", "Initial Infection Rate", 0.02, 0.01, 0.08, 0.01),
    "government_stringent" : UserSettableParameter("slider", "Government Strictness", 0.5, 0.1, 0.9, 0.1),
    "government_action_threshold" : UserSettableParameter("slider", "Government Action Threshold", 0.3, 0.1, 0.9, 0.1),
    "global_aspiration" :UserSettableParameter("slider", "Global Aspiration", 0.3,0.1,0.9,0.1)
}

server = ModularServer(MainModel,
                       [canvas_element, model_legend, space_text_element, line_chart,line_chart_aspiration_comparision],
                       "Infection Model", model_params)