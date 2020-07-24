using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class clicky : MonoBehaviour
{
    [SerializeField] GameObject scoreObject;
    [SerializeField] bool isRubbishBin;
    scorey scorer;
    // Start is called before the first frame update
    
    private void Start()
    {
        scorer = scoreObject.GetComponent<scorey>();
    }
    void OnMouseDown()
    {
        scorer.logScore(Convert.ToInt32(isRubbishBin));
        print("stupiddd"+ Convert.ToInt32(isRubbishBin));
    }

}