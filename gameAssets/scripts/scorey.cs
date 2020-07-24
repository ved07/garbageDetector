using System.Collections;
using System;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class scorey : MonoBehaviour
{
    string[] classArr = {  "recycle", "rubbish" };
    string valueThing;
    string[] arrayOfRecyclableStuff = { "plastic cup", "plastic bottle", "paper bag", "plastic bag", "lined paper", "wooden board", "metal rod", "Cardboard", "green jar", "juice carton", "tin can" };
    string[] arrayOfNonRecyclableStuff = { "food waste", "food-tainted item", "used paper plate", "used styrofoam box", "used paper towels", "ceramic", "kitchenware", "windows", "mirror", "plastic wrap", "packing peanuts" };
    [SerializeField] GameObject textHolder;
    Text gameObjective;
    string output;
    int randomArrIndex;
    int score = 0;
    [SerializeField] GameObject scoreDisplay;
    Text scoreDisp;
    int indexVal;

    System.Random random = new System.Random();
    private void Update()
    {
        if (score == -1)
        {
            SceneManager.LoadScene(2);
        }
    }
    void setObjective()
    {
        var randomIndex = random.Next(0, 2);
        indexVal = randomIndex;
        print(indexVal);
        valueThing = classArr[randomIndex];
        print(valueThing);
        if (valueThing == "rubbish")
        {
            randomArrIndex = random.Next(0, arrayOfNonRecyclableStuff.Length);
            output = arrayOfNonRecyclableStuff[randomArrIndex];
        }
        else
        {
            randomArrIndex = random.Next(0, arrayOfRecyclableStuff.Length);
            output = arrayOfRecyclableStuff[randomArrIndex];
        }
        gameObjective.text = output;


    }
    void Start()
    {
        gameObjective = textHolder.GetComponent<Text>();
        setObjective();
        scoreDisp = scoreDisplay.GetComponent<Text>();
    }
    private IEnumerator StartCounter()
    {
        float countDown = 3f;
        for (int i = 0; i < 3000; i++)
        {
            while (countDown >= 0)
            {
                Debug.Log(i++);
                countDown -= Time.smoothDeltaTime;
                yield return null;
            }
        }

    }
    public void logScore(int returnVal)
    {
        print((indexVal, returnVal));
        if (returnVal==indexVal)
        {
            score += 1;
            gameObjective.text = "correct it was " +  valueThing;
        }
        else
        {
            score -= 1;
            gameObjective.text = "No you were wrong it was actually " + valueThing; 
        }
        
       
        scoreDisp.text = score.ToString();
        setObjective();

    }

}

