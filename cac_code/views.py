from flask import Flask, render_template, request, jsonify
import pandas as pd
import sys

#from stats import total_generated, total_consumed, battery_left,generation_efficiency,hour_avg

#from stats import est_energy_savings,est_co2e_savings,est_car_miles,est_plane_miles,est_trees
#from charts import compare_bar
#from charts import main_line,pie, cons_over_time, corr_heatmap, rec_list

from stats import get_current_usages

from gpt_model import generate_recommendations,create_msgs

from datetime import datetime, timedelta

from app import app

print('BAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh')
@app.route("/",methods=['GET','POST'])
@app.route("/dashboard",methods=['GET','POST'])
def index():
    print('finished running on '+datetime.now().strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00')
    

    print('indexxx')
    return render_template("index.html")
    # return render_template("index.html", 
    #                        graph = main_line, pie=pie, tg=total_generated, tc=total_consumed,
    #                        bl=battery_left, ge=generation_efficiency, ha=hour_avg, heatmap=corr_heatmap     
    #                        )

@app.route("/optimization",methods=['GET','POST'])
def optimization():

    print('optimiiizion')
    return render_template("optimization.html",pie=pie,rec_list=rec_list,
                            line=cons_over_time)

@app.route("/comparison",methods=['GET','POST'])
def comparison():
    print('comparison')
    return render_template("comparison.html",bar=compare_bar, est_energy_savings=est_energy_savings,
                           est_co2e_savings=est_co2e_savings,est_car_miles=est_car_miles,est_plane_miles=est_plane_miles,
                           est_trees=est_trees)

@app.route("/recommendations",methods=['GET','POST'])
def recommendations():
    if request.method == "GET":
        roles = ["system"]
        contents = [["You are an industry expert who advises people on how to lower electricity usage in the home. You are about to be asked by a homeowner about how to reduce energy usage in their home. Please give five concise things the homeowner should do to continue reducing energy consumption in the form of a bullet point list, based on the information that will be provided shortly.  Each tip should include the tip (summary of the idea) and an explanation (why the tip addresses the issue and exactly what needs to be done). Please do not include any solutions that would be a large investment and answer as if you are talking directly to the homeowner. Keep your answer under 2500 characters. Do not repeat advice. Do not use apostrophes or quotations in your answers. Do not include any additional text beyond the 5 bullet points. To indicate a bullet point, use ***. Separate each tip using only a single space and nothing else.","Here is an example interaction with the user:","User: Percentage of energy usage by location in the format {Location: Percentage} for today is {Home office: 25, Fridge: 33, Wine cellar: 17, Garage door: 9, Microwave: 5, Living room: 12}. Percentage of energy usage by location in the format {Location: Percentage} for yesterday is {Home office: 33, Fridge: 26, Wine cellar: 17, Garage door: 6, Microwave: 4, Living room: 14}. Do not repeat any advice that you have given me in the past.","Assistant (you): *** Unplug unused electronics: Unplug any electronics that are not actively being used to reduce their standby power consumption. Unused home office equipment could contribute to a significant portion of energy usage, accounting for 25% today and 33% yesterday. *** Adjust refrigerator temperature: Adjust the temperature setting of the refrigerator to optimize energy efficiency. It may have been set too low, leading to excessive energy consumption. The fridge is responsible for 33% of energy usage today and 26% yesterday. *** Optimize wine cellar usage: Minimize wine cellar usage or reduce the temperature setting to reduce energy consumption. While the wine cellar contributes only 17% to energy usage, it remains consistently high both yesterday and today. *** Insulate garage doors: Improve the insulation of the garage door to prevent air leakage, especially if it is responsible for 9% of the energy usage today and 6% yesterday. This will reduce the amount of heating or cooling required for this area, resulting in energy savings. *** Use microwave sparingly: Minimize the use of the microwave, which accounts for 5% of energy usage today and 4% yesterday. Consider using alternative cooking methods, such as stovetop or oven, for certain meals when feasible. *** Optimize living room lighting: Replace inefficient light bulbs with energy-efficient LEDs in the living room and utilize natural lighting whenever possible. The living room contributes to 12% of energy usage, so improving lighting efficiency can make a noticeable difference."]]
        # msgs = [
        #     {
        #     "role": "system",
        #     "content": "You are an industry expert who advises people on how to lower electricity usage in the home. You are about to be asked by a homeowner about how to reduce energy usage in their home. Please give five concise things the homeowner should do to continue reducing energy consumption in the form of a bullet point list, based on the information that will be provided shortly.  Each tip should include the tip (summary of the idea) and an explanation (why the tip addresses the issue and exactly what needs to be done). Please do not include any solutions that would be a large investment and answer as if you are talking directly to the homeowner. Keep your answer under 2500 characters. Do not repeat advice. Do not use apostrophes or quotations in your answers.\nHere is an example interaction with the user:\nUser: Percentage of energy usage by location in the format {Location: Percentage} for today:\n{Home office: 25, Fridge: 33, Wine cellar: 17, Garage door: 9, Microwave: 5, Living room: 12}\nPercentage of energy usage by location in the format {Location: Percentage} for yesterday:\n{Home office: 33, Fridge: 26, Wine cellar: 17, Garage door: 6, Microwave: 4, Living room: 14}\n\nAssistant (you): 1. Unplug unused electronics: Unplug any electronics that are not actively being used to reduce their standby power consumption. Unused home office equipment could contribute to a significant portion of energy usage, accounting for 25% today and 33% yesterday.\n2. Adjust refrigerator temperature: Adjust the temperature setting of the refrigerator to optimize energy efficiency. It may have been set too low, leading to excessive energy consumption. The fridge is responsible for 33% of energy usage today and 26% yesterday.\n3. Optimize wine cellar usage: Minimize wine cellar usage or reduce the temperature setting to reduce energy consumption. While the wine cellar contributes only 17% to energy usage, it remains consistently high both yesterday and today.\n4. Insulate garage doors: Improve the insulation of the garage door to prevent air leakage, especially if it is responsible for 9% of the energy usage today and 6% yesterday. This will reduce the amount of heating or cooling required for this area, resulting in energy savings.\n5. Use microwave sparingly: Minimize the use of the microwave, which accounts for 5% of energy usage today and 4% yesterday. Consider using alternative cooking methods, such as stovetop or oven, for certain meals when feasible.\n6. Optimize living room lighting: Replace inefficient light bulbs with energy-efficient LEDs in the living room and utilize natural lighting whenever possible. The living room contributes to 12% of energy usage, so improving lighting efficiency can make a noticeable difference."
        #     },
        # ]
        print('recommendations')
        return render_template("recommendations.html",roles=roles,contents=contents)
    # elif request.method == 'POST':
    #     if len(msgs) == 1:
    #         msgs.append(
    #             {
    #             "role": "user",
    #             "content": "User: Today's percentage of energy usage by location in the format {Location: Percentage}:\n{Home office: 25, Fridge: 33, Wine cellar: 17, Garage door: 9, Microwave: 5, Living room: 12}\nYesterday's percentage of energy usage by location in the format [Location: Percentage]:{Home office: 33, Fridge: 26, Wine cellar: 17, Garage door: 6, Microwave: 4, Living room: 14}"
    #             }
    #         )
    #     else:
    #         msgs.append(
    #             {
    #             "role": "user",
    #             "content": "Give me another five tips based on my original information. Do not repeat any advice that you have given me in the past."
    #             }
    #         )

    #     finish_reason, content = generate_recommendations(msgs)

    #     msgs.append({"role": "assistant", "content": content})
    #     print(msgs)
    #     return jsonify({"error": "0", "content": content})

@app.route("/genrec", methods=['GET','POST'])
def genrec():
    print('genrec')
    # msgs = [
    #     {
    #     "role": "system",
    #     "content": "You are an industry expert who advises people on how to lower electricity usage in the home. You are about to be asked by a homeowner about how to reduce energy usage in their home. Please give three concise things the homeowner should do to continue reducing energy consumption in the form of a bullet point list, based on the information that will be provided shortly.  Each tip should include the tip (summary of the idea) and an explanation (why the tip addresses the issue and exactly what needs to be done). Please don't include any solutions that would be a large investment and answer as if you are talking directly to the homeowner. Keep your answer under 1500 characters. Do not repeat advice.\n\nHere is an example interaction with the user:\nUser: Today's percentage of energy usage by location in the format {Location: Percentage}:\n{\"Home office\": 25, \"Fridge\": 33, \"Wine cellar\": 17, \"Garage door\": 9, \"Microwave: 5, \"Living room\": 12}\nYesterday's percentage of energy usage by location in the format [Location: Percentage]:\n{\"Home office\": 33, \"Fridge\": 26, \"Wine cellar\": 17, \"Garage door\": 6, \"Microwave: 4, \"Living room\": 14}\n\nAssistant (you): 1. Unplug unused electronics: Unplug any electronics that are not actively being used to reduce their standby power consumption. Unused home office equipment could contribute to a significant portion of energy usage, accounting for 25% today and 33% yesterday.\n2. Adjust refrigerator temperature: Adjust the temperature setting of the refrigerator to optimize energy efficiency. It may have been set too low, leading to excessive energy consumption. The fridge is responsible for 33% of energy usage today and 26% yesterday.\n3. Optimize wine cellar usage: Minimize wine cellar usage or reduce the temperature setting to reduce energy consumption. While the wine cellar contributes only 17% to energy usage, it remains consistently high both yesterday and today.\n4. Insulate garage doors: Improve the insulation of the garage door to prevent air leakage, especially if it is responsible for 9% of the energy usage today and 6% yesterday. This will reduce the amount of heating or cooling required for this area, resulting in energy savings.\n5. Use microwave sparingly: Minimize the use of the microwave, which accounts for 5% of energy usage today and 4% yesterday. Consider using alternative cooking methods, such as stovetop or oven, for certain meals when feasible.\n6. Optimize living room lighting: Replace inefficient light bulbs with energy-efficient LEDs in the living room and utilize natural lighting whenever possible. The living room contributes to 12% of energy usage, so improving lighting efficiency can make a noticeable difference."
    #     },
    #     {
    #     "role": "user",
    #     "content": "User: Today's percentage of energy usage by location in the format {Location: Percentage}:\n{Home office: 25, Fridge: 33, Wine cellar: 17, Garage door: 9, Microwave: 5, Living room: 12}\nYesterday's percentage of energy usage by location in the format [Location: Percentage]:{Home office: 33, Fridge: 26, Wine cellar: 17, Garage door: 6, Microwave: 4, Living room: 14}"
    #     }
    # ]
    roles = request.get_json()['roles']
    contents = request.get_json()['contents']
    # print(roles)
    # print(type(roles))
    # print(contents)
    # print(type(contents))
    print(roles)
    if len(roles) >= 13:
        roles.pop(1)
        roles.pop(1)
        contents.pop(1)
        contents.pop(1)
        print("OH NO!")
        print(roles)
    

    # get percentage data, then format into whatever i used earlier
    data = get_current_usages()
    print("aaaaaaaaaaaaaaaaa")
    print(data)
    roles.append("user")
    contents.append([data])
    msgs = create_msgs(roles,contents)
    # msgs.append({"role": "user", "content": data})
    print(msgs)
    finish_reason, content = generate_recommendations(msgs)
    print(content)
    roles.append("assistant")
    contents.append(content)

    return jsonify({"error": "0", "roles": roles, "contents": contents})