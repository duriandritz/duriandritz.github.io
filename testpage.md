---
layout: base
title: "DIY Stats - Statistical Test Selector"
permalink: /testpage
---
<body style="background-color: white">
    <header class="navbar navbar-expand-md p-0">
        <div class="container p-0 pt-2">
            <nav class="container mx-3">
                <div class="d-flex align-items-center justify-content-center justify-content-lg-start py-1" role="navigation">
                    <a href="#" class="navbar-brand d-flex mb-lg-0 me-1">
                        <svg xmlns="http://www.w3.org/2000/svg" role="img" width="30" height="30" fill="black" class="bi bi-rocket-takeoff" viewBox="0 0 16 16">
                            <path d="M9.752 6.193c.599.6 1.73.437 2.528-.362s.96-1.932.362-2.531c-.599-.6-1.73-.438-2.528.361-.798.8-.96 1.933-.362 2.532"/>
                            <path d="M15.811 3.312c-.363 1.534-1.334 3.626-3.64 6.218l-.24 2.408a2.56 2.56 0 0 1-.732 1.526L8.817 15.85a.51.51 0 0 1-.867-.434l.27-1.899c.04-.28-.013-.593-.131-.956a9 9 0 0 0-.249-.657l-.082-.202c-.815-.197-1.578-.662-2.191-1.277-.614-.615-1.079-1.379-1.275-2.195l-.203-.083a10 10 0 0 0-.655-.248c-.363-.119-.675-.172-.955-.132l-1.896.27A.51.51 0 0 1 .15 7.17l2.382-2.386c.41-.41.947-.67 1.524-.734h.006l2.4-.238C9.005 1.55 11.087.582 12.623.208c.89-.217 1.59-.232 2.08-.188.244.023.435.06.57.093q.1.026.16.045c.184.06.279.13.351.295l.029.073a3.5 3.5 0 0 1 .157.721c.055.485.051 1.178-.159 2.065m-4.828 7.475.04-.04-.107 1.081a1.54 1.54 0 0 1-.44.913l-1.298 1.3.054-.38c.072-.506-.034-.993-.172-1.418a9 9 0 0 0-.164-.45c.738-.065 1.462-.38 2.087-1.006M5.205 5c-.625.626-.94 1.351-1.004 2.09a9 9 0 0 0-.45-.164c-.424-.138-.91-.244-1.416-.172l-.38.054 1.3-1.3c.245-.246.566-.401.91-.44l1.08-.107zm9.406-3.961c-.38-.034-.967-.027-1.746.163-1.558.38-3.917 1.496-6.937 4.521-.62.62-.799 1.34-.687 2.051.107.676.483 1.362 1.048 1.928.564.565 1.25.941 1.924 1.049.71.112 1.429-.067 2.048-.688 3.079-3.083 4.192-5.444 4.556-6.987.183-.771.18-1.345.138-1.713a3 3 0 0 0-.045-.283 3 3 0 0 0-.3-.041Z"/>
                            <path d="M7.009 12.139a7.6 7.6 0 0 1-1.804-1.352A7.6 7.6 0 0 1 3.794 8.86c-1.102.992-1.965 5.054-1.839 5.18.125.126 3.936-.896 5.054-1.902Z"/>
                        </svg>
                    </a>
                    <div class="collapse navbar-collapse">
                        <ul class="nav col-lg-auto me-auto mb-2 justify-content-center mb-md-0">
                            <li><a href="#" class="nav-link px-2 text-dark">DIY Stats</a></li>
                            <li>
                                <button type="button" data-bs-toggle="modal" data-bs-target="#pmodal" class="nav-link px-2 text-secondary">Statistical Test Selector</button>
                            </li>
                            <!-- Project Modal-->
                            <div class="modal fade" id="pmodal" tabindex="-1" aria-labelledby="pmodalLabel" aria-hidden="true">
                                <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <h1 class="modal-title fs-5" id="ContactUsLabel">Statistical Test Selector - How to Use</h1>
                                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                        </div>
                                        <div class="modal-body">
                                                <p>You are here because you are one of the following:</p>
                                                <ul>
                                                    <li>a student enrolled in an inferential statistics course;</li>
                                                    <li>a researcher unsure of what statistical test to use;</li>
                                                    <li>a data analyst that needs to look up the basics; or</li>
                                                    <li>you just really love stats.</li>
                                                </ul>
                                                <br>
                                                <p>
                                                    In any case, this web app might just be what you're looking for!
                                                </p>
                                                <p>
                                                    The Statistical Test Selector is designed to be a self-help guide using
                                                    only simple questions about your research question, variable/s, and
                                                    assumptions about the population of interest.
                                                </p>
                                                <p>
                                                    For most of the tests recommended, it is assumed that your sample was
                                                    selected using simple random sampling, or that you have followed the necessary
                                                    protocols for randomization in experiments.
                                                </p>
                                                <p>
                                                    If you have comments or suggestions, please feel free to contact us through our
                                                    connected channels. As always,
                                                </p>
                                                <p>
                                                    It's not Rocket Science, it's just Stats!
                                                </p>
                                        </div>
                                        <div class="modal-footer">
                                            <!-- <h6 style="font-size: 12px"> -->
                                                <p>
                                                    This web application was inspired by
                                                    <a href="https://statisticaldecisiontree.microsiris.com/default.htm">The Decision Tree for Statistics</a>
                                                    (2014) by Neal Van Eck. Rocket Scientist Teachers does not claim to own any copyrighted content
                                                    that may have been used in this web application.
                                                </p>
                                            <!-- </h6> -->
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </ul>
                <ul class="nav col-lg-auto mb-2 justify-content-center mb-md-0">
                    <li class="nav-item dropdown-center">
                        <a class="nav-link dropdown-toggle px-2 text-secondary" href="#" data-bs-toggle="dropdown" aria-expanded="false">Other Tools</a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="/statisticaltestselector">Statistical Test Selector</a></li>
                            <li><hr class="dropdown-divider"></li>
                            <li><h6 class="dropdown-header">Coming Soon</h6></li>
                            <li><a class="dropdown-item disabled" href="#">Experimental Design Layout Builder</a></li>
                            <li><a class="dropdown-item disabled" href="#">Probability Distribution Visualizer</a></li>
                        </ul>
                    </li>
                    <li>
                        <button type="button" data-bs-toggle="modal" data-bs-target="#AboutUs" class="nav-link px-2 text-secondary">About</button>
                    </li>
                    <li>
                        <button type="button" data-bs-toggle="modal" data-bs-target="#ContactUs" class="nav-link px-2 text-secondary">Contact Us</button>
                    </li>
                </ul>
            </div>
                </div>
            </nav>
        </div>
    </header>

    <main class="container-fluid d-flex py-2 text-center">
<div class="bg-gradient container-fluid border border-3 rounded-3 shadow-lg" style="width: 680px; height: 600px; background-color: #69a6ffa1; border-color: black !important; --bs-gradient: linear-gradient(180deg, rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0))">
    <p class="fw-semibold" style="font-family: 'League Spartan', sans-serif; margin-bottom: -2px">STATISTICAL TEST SELECTOR</p>
    <div class ="container-fluid border border-2 overflow-y-auto rounded-3" style="height: 522px; padding-top: 15px; margin-bottom: 7px; background-color: white; border-color: black !important">
        <h5>In choosing your statistical test, first identify the problem/objective that you wish to solve.</h5>
        <h6>Afterwards, answer the questions below in sequence.</h6>
    <!-- Div 1: Using Flask to Automate the Questions and Answers-->
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p1" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>How many variables are in your problem?
                </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a1" data-target="p2" data-source="p1">
                            One Variable
                        </button>
                        <button class="answer btn btn-primary" id="a2" data-target="p3" data-source="p1">
                            Two Variables
                        </button>
                        <button class="answer btn btn-primary" id="a3" data-target="p4" data-source="p1">
                            More than Two Variables
                        </button>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p2" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>What is the Level of Measurement of the variable?
<sup>[<a href="https://stats.libretexts.org/Workbench/Statistics_for_Behavioral_Science_Majors/01%3A_Naming_Collecting_Data_and_Research_Design/1.04%3A_Levels_of_Measurement" target = "_blank" title="Level of Measurement">1</a>]</sup>                    </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a4" data-target="p5" data-source="p2">
                            Nominal
                        </button>
                        <button class="answer btn btn-primary" id="a10" data-target="p11" data-source="p2">
                            Ordinal
                        </button>
                        <button class="answer btn btn-primary" id="a11" data-target="p12" data-source="p2">
                            Interval or Ratio
                        </button>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p3" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Which of the following best describes your objective?
                </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a9" data-target="p10" data-source="p3">
                            Differences Between Groups
                        </button>
                        <button class="answer btn btn-primary" id="a21" data-target="p22" data-source="p3">
                            Relationship Between Variables
                        </button>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p4" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Which of the following best describes your objective?
                </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a27" data-target="p28" data-source="p4">
                            Factors Affecting a Response Variable
                        </button>
                        <button class="answer btn btn-primary" id="a30" data-target="p31" data-source="p4">
                            Relationships Between Variables
                        </button>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p5" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>What would you like to know about the variable?
                </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a5" data-target="p6" data-source="p5">
                            Distribution
                        </button>
                        <button class="answer btn btn-primary" id="a18" data-target="p19" data-source="p5">
                            Other
                        </button>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p6" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Goodness-of-Fit Test for Binomial/Multinomial Distributions
<sup>[<a href="https://online.stat.psu.edu/stat504/Lesson02#goodness-of-fit-test" target = "_blank" title="Goodness-of-Fit Test">2</a>]</sup><sup>[<a href="https://online.stat.psu.edu/stat200/lesson/8/8.1/8.1.2" target = "_blank" title="Alternative: One Sample Proportion Z-test">alt</a>]</sup>                    </h6>
                    <h7>Use this to determine if your observed data fits a hypothesized distribution. 
<br>
<br>Some examples:
<br>Do the phenotypes exhibit an equal distribution?
<br>Do the voters prefer a certain candidate compared to others?</h7>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p10" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>How many levels are there in the grouping variable?
                </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a22" data-target="p23" data-source="p10">
                            Two
                        </button>
                        <button class="answer btn btn-primary" id="a23" data-target="p24" data-source="p10">
                            More than Two
                        </button>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p11" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>What would you like to know about the variable?
                </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a14" data-target="p16" data-source="p11">
                            Measures of Central Tendency
                        </button>
                        <button class="answer btn btn-primary" id="a15" data-target="p15" data-source="p11">
                            Distribution
                        </button>
                        <button class="answer btn btn-primary" id="a69" data-target="p70" data-source="p11">
                            Dispersion
                        </button>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p12" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>What would you like to know about the variable?
                </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a12" data-target="p13" data-source="p12">
                            Measures of Central Tendency
                        </button>
                        <button class="answer btn btn-primary" id="a37" data-target="p38" data-source="p12">
                            Distribution
                        </button>
                        <button class="answer btn btn-primary" id="a38" data-target="p39" data-source="p12">
                            Dispersion
                        </button>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p13" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Are you willing to assume that the variable is Normally Distributed?
<sup>[<a href="https://stats.libretexts.org/Workbench/Statistics_for_Behavioral_Science_Majors/05%3A_Continuous_Probability_Distributions/5.03%3A_Normal_Distribution_and_Its_Applications" target = "_blank" title="Normal Distribution">2</a>]</sup>                    </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a13" data-target="p14" data-source="p13">
                            Yes
                        </button>
                        <button class="answer btn btn-primary" id="a39" data-target="p40" data-source="p13">
                            No
                        </button>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p14" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Is the population variance known?
<sup>[<a href="https://stats.libretexts.org/Workbench/Statistics_for_Behavioral_Science_Majors/01%3A_Naming_Collecting_Data_and_Research_Design/1.02%3A_Definitions_of_Statistics_and_Key_Terms#Definition:_Population" target = "_blank" title="Population">3</a>]</sup>                    </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a40" data-target="p41" data-source="p14">
                            Yes
                        </button>
                        <button class="answer btn btn-primary" id="a41" data-target="p42" data-source="p14">
                            No
                        </button>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p15" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Goodness-of-Fit Test for Binomial/Multinomial Distributions
<sup>[<a href="https://online.stat.psu.edu/stat504/Lesson02#goodness-of-fit-test" target = "_blank" title="Goodness-of-Fit Test">2</a>]</sup>                    </h6>
                    <h7>Ordinal Variables are still considered categorical variables. Use this test to determine if your observed data fits a hypothesized distribution. 
<br>
<br>Example:
<br>Are all age groups equally represented?</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p16" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Sign Test for One Population Median
<sup>[<a href="https://stats.libretexts.org/Workbench/Statistics_for_Behavioral_Science_Majors/12%3A_Nonparametric_Tests/12.02%3A_Sign_Test" target = "_blank" title="Sign Test">2</a>]</sup><sup>[<a href="https://math.montana.edu/jobo/thainp/onesamp.pdf" target = "_blank" title="Sign Test">3</a>]</sup><sup>[<a href="https://math.montana.edu/jobo/thainp/onesamp.pdf" target = "_blank" title="Alternative: Wilcoxon Signed-Rank Test">alt</a>]</sup>                    </h6>
                    <h7>Use this test to test for the value of the median of a distribution. The Sign Test uses a binomial distribution to test if 50% of the values are above (or below) the hypothesized median value.
<br>
<br>Example:
<br>Is the median BMI of the participants overweight? (Which is the same as: Are 50% of the participants at least overweight?)</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p19" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>The Statistical Test Selector does not yet include other tests for a single Nominal Variable.
                </h6>
                    <h7>Recommendation: Review your objective if it needs tests or simply descriptive statistics.</h7>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p22" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Are your variables both categorical - i.e. Nominal or Ordinal?
<sup>[<a href="
https://stats.libretexts.org/Workbench/Statistics_for_Behavioral_Science_Majors/01%3A_Naming_Collecting_Data_and_Research_Design/1.04%3A_Levels_of_Measurement" target = "_blank" title="Level of Measurement">1</a>]</sup>                    </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a35" data-target="p36" data-source="p22">
                            Yes
                        </button>
                        <button class="answer btn btn-primary" id="a79" data-target="p80" data-source="p22">
                            No
                        </button>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p23" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Which of the following best describes the parameter of interest?
<sup>[<a href="https://stats.libretexts.org/Courses/Lumen_Learning/Concepts_in_Statistics_(Lumen)/07%3A_Linking_Probability_to_Statistical_Inference/7.03%3A_Parameters_vs._Statistics" target = "_blank" title="Parameter">1</a>]</sup>                    </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a25" data-target="p26" data-source="p23">
                            Proportions
                        </button>
                        <button class="answer btn btn-primary" id="a26" data-target="p27" data-source="p23">
                            Means
                        </button>
                        <button class="answer btn btn-primary" id="a48" data-target="p49" data-source="p23">
                            Medians
                        </button>
                        <button class="answer btn btn-primary" id="a49" data-target="p50" data-source="p23">
                            Variances
                        </button>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p24" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Which of the following best describes the parameter of interest?
<sup>[<a href="https://stats.libretexts.org/Courses/Lumen_Learning/Concepts_in_Statistics_(Lumen)/07%3A_Linking_Probability_to_Statistical_Inference/7.03%3A_Parameters_vs._Statistics" target = "_blank" title="Parameter">1</a>]</sup>                    </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a46" data-target="p47" data-source="p24">
                            Means
                        </button>
                        <button class="answer btn btn-primary" id="a47" data-target="p48" data-source="p24">
                            Other
                        </button>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p26" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Are the samples matched/paired?
                </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a44" data-target="p45" data-source="p26">
                            Yes
                        </button>
                        <button class="answer btn btn-primary" id="a45" data-target="p46" data-source="p26">
                            No
                        </button>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p27" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Are the samples matched/paired?
                </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a50" data-target="p51" data-source="p27">
                            Yes
                        </button>
                        <button class="answer btn btn-primary" id="a51" data-target="p52" data-source="p27">
                            No
                        </button>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p28" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>What is the level of measurement of the response variable?
<sup>[<a href="https://stats.libretexts.org/Workbench/Statistics_for_Behavioral_Science_Majors/01%3A_Naming_Collecting_Data_and_Research_Design/1.04%3A_Levels_of_Measurement" target = "_blank" title="Level of Measurement">1</a>]</sup>                    </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a28" data-target="p63" data-source="p28">
                            Nominal or Ordinal
                        </button>
                        <button class="answer btn btn-primary" id="a62" data-target="p29" data-source="p28">
                            Interval or Ratio
                        </button>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p29" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Are the factors variables of interest all categorical?
                </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a65" data-target="p66" data-source="p29">
                            Yes
                        </button>
                        <button class="answer btn btn-primary" id="a66" data-target="p67" data-source="p29">
                            No
                        </button>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p31" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Are all variables at least interval level?
                </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a67" data-target="p68" data-source="p31">
                            Yes
                        </button>
                        <button class="answer btn btn-primary" id="a68" data-target="p69" data-source="p31">
                            No
                        </button>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p36" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Test for Independence
<sup>[<a href="https://online.stat.psu.edu/stat504/Lesson03#test-for-independence" target = "_blank" title="Test for Independence">2</a>]</sup>                    </h6>
                    <h7>Use this to determine if the variables are associated with (or dependent on) each other.
<br>
<br>Example:
<br>Is voter preference independent of income class?</h7>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p38" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Are you testing for normality?
<sup>[<a href="https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Introductory_Statistics_(Lane)/07%3A_Normal_Distribution/7.01%3A_Introduction_to_Normal_Distributions" target = "_blank" title="Normality">2</a>]</sup>                    </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a54" data-target="p55" data-source="p38">
                            Yes
                        </button>
                        <button class="answer btn btn-primary" id="a55" data-target="p56" data-source="p38">
                            No
                        </button>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p39" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Are you willing to assume that the population is normally distributed?
<sup>[<a href="https://stats.libretexts.org/Workbench/Statistics_for_Behavioral_Science_Majors/01%3A_Naming_Collecting_Data_and_Research_Design/1.02%3A_Definitions_of_Statistics_and_Key_Terms#Definition:_Population" target = "_blank" title="Population">2</a>]</sup><sup>[<a href="https://stats.libretexts.org/Workbench/Statistics_for_Behavioral_Science_Majors/05%3A_Continuous_Probability_Distributions/5.03%3A_Normal_Distribution_and_Its_Applications" target = "_blank" title="Normal Distribution">3</a>]</sup>                    </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a70" data-target="p71" data-source="p39">
                            Yes
                        </button>
                        <button class="answer btn btn-primary" id="a71" data-target="p72" data-source="p39">
                            No
                        </button>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p40" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>The Statistical Test Selector does not yet have this type of test.
<sup>[<a href="https://stats.libretexts.org/Courses/Colby_College/EC225%3A_Research_Methods_and_Statistics_for_Economics/New_Page/13%3A_Nonparametric_Tests_(not_covered_in_EC225)/13.03%3A_Ranking_Data" target = "_blank" title="Ranks">3</a>]</sup>                    </h6>
                    <h7>Recommendation: Transform the variable of interest into binary or ranks and test for the median instead of the mean.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p41" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Z-Test for One Population Mean
<sup>[<a href="https://online.stat.psu.edu/stat200/lesson/8/8.2/8.2.3/8.2.3.3" target = "_blank" title="One Sample Mean Z-Test">4</a>]</sup>                    </h6>
                    <h7>This test can be used to test for the mean of a normally distributed continuous variable with known population variance.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p42" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>t-Test for One Population Mean
<sup>[<a href="https://online.stat.psu.edu/stat200/lesson/8/8.2/8.2.3/8.2.3.1" target = "_blank" title="One Sample Mean t-Test">4</a>]</sup>                    </h6>
                    <h7>This test can be used to test for the mean of a normally distributed variable.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p44" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Dependent Samples t-test for Population Mean Difference
                </h6>
                    <h7>Use this test if you have two matched samples and would like to test the mean.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p45" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>McNemar&#39;s Test
<sup>[<a href="https://stats.libretexts.org/Bookshelves/Applied_Statistics/Mikes_Biostatistics_Book_(Dohm)/09%3A_Categorical_Data/9.6%3A_McNemar" target = "_blank" title="McNemar&#39;s Test">2</a>]</sup>                    </h6>
                    <h7>Use this test if you want to test for the difference between two proportions from two matched/paired samples.
<br>
<br>Example:
<br>Is the proportion of students that passed the exam the same before and after remedial classes?</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p46" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Fisher&#39;s Exact Test
<sup>[<a href="https://online.stat.psu.edu/stat504/Lesson04#fishers-exact-test" target = "_blank" title="Fisher&#39;s Exact Test">2</a>]</sup><sup>[<a href="https://stats.libretexts.org/Bookshelves/Applied_Statistics/Biological_Statistics_(McDonald)/02%3A_Tests_for_Nominal_Variables/2.05%3A_Chi-square_Test_of_Independence" target = "_blank" title="Alternative: Chi-Square Test of Independence">alt</a>]</sup><sup>[<a href="https://stats.libretexts.org/Bookshelves/Applied_Statistics/Biological_Statistics_(McDonald)/02%3A_Tests_for_Nominal_Variables/2.06%3A_GTest_of_Independence" target = "_blank" title="Alternative: G-Test of Independence">alt</a>]</sup>                    </h6>
                    <h7>Use this test to test for the difference in proportions of two independent groups.
<br>
<br>Example:
<br>Is the proportion of voters that favor a particular candidate the same for both regions?</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p47" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>F-test using One-Way Analysis of Variance
<sup>[<a href="https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Statistics_with_Technology_2e_(Kozak)/11%3A_Chi-Square_and_ANOVA_Tests/11.03%3A_Analysis_of_Variance_(ANOVA)" target = "_blank" title="ANOVA">2</a>]</sup><sup>[<a href="https://courses.washington.edu/psy524a/_book/nonparametric-tests.html#kruskal-wallis-one-way-anova" target = "_blank" title="Alternative: Kruskal-Wallis">alt</a>]</sup>                    </h6>
                    <h7>Use this test in combination with ANOVA to test for the differences in the means between three or more groups.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p48" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>The Statistical Test Selector does not yet include a test for this selection.
                </h6>
                    <h7></h7>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p49" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Are the samples matched/paired?
                </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a72" data-target="p73" data-source="p49">
                            Yes
                        </button>
                        <button class="answer btn btn-primary" id="a74" data-target="p75" data-source="p49">
                            No
                        </button>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p50" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Are the samples matched/paired?
                </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a75" data-target="p76" data-source="p50">
                            Yes
                        </button>
                        <button class="answer btn btn-primary" id="a76" data-target="p77" data-source="p50">
                            No
                        </button>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p51" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Are you willing to assume that the distribution of the paired differences is normally distributed?
<sup>[<a href="https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Introductory_Statistics_(Lane)/07%3A_Normal_Distribution/7.01%3A_Introduction_to_Normal_Distributions" target = "_blank" title="Normality">2</a>]</sup>                    </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a52" data-target="p53" data-source="p51">
                            Yes
                        </button>
                        <button class="answer btn btn-primary" id="a53" data-target="p54" data-source="p51">
                            No
                        </button>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p52" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Are you willing to assume that both groups are normally distributed?
<sup>[<a href="https://stats.libretexts.org/Workbench/Statistics_for_Behavioral_Science_Majors/05%3A_Continuous_Probability_Distributions/5.03%3A_Normal_Distribution_and_Its_Applications" target = "_blank" title="Normal Distribution">2</a>]</sup>                    </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a56" data-target="p57" data-source="p52">
                            Yes
                        </button>
                        <button class="answer btn btn-primary" id="a57" data-target="p58" data-source="p52">
                            No
                        </button>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p53" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Dependent Samples t-test for Population Mean Difference
<sup>[<a href="https://online.stat.psu.edu/stat200/lesson/8/8.3/8.3.2" target = "_blank" title="Matched Pairs t-Test">3</a>]</sup>                    </h6>
                    <h7>Use this test if you have two matched samples and would like to test the mean of the paired differences.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p54" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>The Statistical Test Selector does not yet include a test for difference in means with non-normal populations.
                </h6>
                    <h7>Recommendation: Transform the variable into ranks and test for the median difference instead of means.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p55" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Wilk-Shapiro Test for Normality
<sup>[<a href="https://courses.washington.edu/psy524a/_book/tests-for-homogeneity-of-variance-and-normality.html#the-shapiro-wilk-test" target = "_blank" title="Wilk-Shapiro Test">3</a>]</sup>                    </h6>
                    <h7>Use this test to test if your sample comes from a normal distribution.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p56" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Kolmogorov-Smirnov Test for Distribution
<sup>[<a href="https://online.stat.psu.edu/stat415/lesson/22" target = "_blank" title="Kolmogorov-Smirnov Test">3</a>]</sup>                    </h6>
                    <h7>Use this test to test if your sample comes from a hypothesized distribution.</h7>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p57" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Is the population variance known for both groups?
<sup>[<a href="https://stats.libretexts.org/Workbench/Statistics_for_Behavioral_Science_Majors/01%3A_Naming_Collecting_Data_and_Research_Design/1.02%3A_Definitions_of_Statistics_and_Key_Terms#Definition:_Population" target = "_blank" title="Population">3</a>]</sup>                    </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a58" data-target="p59" data-source="p57">
                            Yes
                        </button>
                        <button class="answer btn btn-primary" id="a59" data-target="p60" data-source="p57">
                            No
                        </button>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p58" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>The Statistical Test Selector does not yet have this type of test.
                </h6>
                    <h7>Recommendation: Transform the variable of interest into ranks and test for medians instead of means.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p59" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Z-test for Two Population Means
<sup>[<a href="https://stats.libretexts.org/Courses/Citrus_College/Statistics_C1000%3A_Introduction_to_Statistics/09%3A_Hypothesis_Testing_for_Two_Samples/9.01%3A_z-Test_for_the_Difference_Between_Two_Means" target = "_blank" title="Z-test for Two Means">4</a>]</sup>                    </h6>
                    <h7>Use this test to test for the difference in the means of two normally distributed random samples with known population variances.</h7>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p60" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Are you willing to assume that both groups have equal population variances?
<sup>[<a href="https://stats.libretexts.org/Workbench/Statistics_for_Behavioral_Science_Majors/01%3A_Naming_Collecting_Data_and_Research_Design/1.02%3A_Definitions_of_Statistics_and_Key_Terms#Definition:_Population" target = "_blank" title="Population">4</a>]</sup>                    </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a60" data-target="p61" data-source="p60">
                            Yes
                        </button>
                        <button class="answer btn btn-primary" id="a61" data-target="p62" data-source="p60">
                            No
                        </button>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p61" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Independent Samples t-test
<sup>[<a href="https://stats.libretexts.org/Courses/Citrus_College/Statistics_C1000%3A_Introduction_to_Statistics/09%3A_Hypothesis_Testing_for_Two_Samples/9.02%3A__t-Test_for_the_Difference_Between_Two_Means" target = "_blank" title="t-Test for Two Means">5</a>]</sup>                    </h6>
                    <h7>Use this test to test for the difference in the means of two normally distributed samples with equal variances.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p62" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Welch&#39;s t-test
<sup>[<a href="https://stats.libretexts.org/Courses/Cerritos_College/Introduction_to_Statistics_with_R/11%3A_Comparing_Two_Means/11.04%3A_The_Independent_Samples_t-test_(Welch_Test)" target = "_blank" title="Welch&#39;s Test">5</a>]</sup>                    </h6>
                    <h7>Use this test to test for the difference in means of two normally distributed random samples with different variances.</h7>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p63" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>How many levels are there in the categorical response variable?
                </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a63" data-target="p64" data-source="p63">
                            Two
                        </button>
                        <button class="answer btn btn-primary" id="a64" data-target="p65" data-source="p63">
                            More than Two
                        </button>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p64" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Binary Logistic Regression
<sup>[<a href="https://online.stat.psu.edu/stat462/node/207/" target = "_blank" title="Logistic Regression">2</a>]</sup>                    </h6>
                    <h7>Use this method for modeling the probabilities of a binary variable using predictor variables.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p65" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Multinomial Logistic Regression
<sup>[<a href="https://online.stat.psu.edu/stat504/Lesson08" target = "_blank" title="Multinomial Logistic Regression">2</a>]</sup>                    </h6>
                    <h7>Use this method when there are more than two categories in the response variable.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p66" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Analysis of Variance
<sup>[<a href="https://online.stat.psu.edu/stat500/Lesson10" target = "_blank" title="ANOVA">2</a>]</sup>                    </h6>
                    <h7>Use this method in conjunction with multiple F-tests to determine the significant factors that affect your response variable.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p67" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Multiple Linear Regression
<sup>[<a href="https://online.stat.psu.edu/stat462/node/131/" target = "_blank" title="Multiple Linear Regression">2</a>]</sup>                    </h6>
                    <h7>Use this method in conjunction with multiple F-tests to determine the factors that affect your response variable.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p68" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Partial Correlations
<sup>[<a href="https://online.stat.psu.edu/stat505/Lesson06#testing-for-partial-correlation" target = "_blank" title="Partial Correlation">1</a>]</sup>                    </h6>
                    <h7>Use this to test for relationships between pairs of variables while accounting for possible variance from other variables.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p69" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>The Statistical Test Selector does not yet include a test for this selection.
                </h6>
                    <h7></h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p70" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>The Statistical Test Selector does not include tests regarding dispersion of an Ordinal Variable.
<sup>[<a href="https://stats.libretexts.org/Courses/Fort_Hays_State_University/Elements_of_Statistics/02%3A_Descriptive_Statistics/2.06%3A_Measures_of_Dispersion#Interquartile_Range" target = "_blank" title="Inter-Quartile Range">2</a>]</sup><sup>[<a href="https://stats.libretexts.org/Courses/Fort_Hays_State_University/Elements_of_Statistics/02%3A_Descriptive_Statistics/2.06%3A_Measures_of_Dispersion#Range" target = "_blank" title="Range">3</a>]</sup>                    </h6>
                    <h7>Recommendation: Instead, use Range or IQR to compare dispersion across multiple variables with the same scale. Note that this does not constitute a statistical test.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p71" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Chi-Square Test for One Population Variance
<sup>[<a href="https://online.stat.psu.edu/stat415/lesson/12/12.1" target = "_blank" title="Chi-Square Test">4</a>]</sup>                    </h6>
                    <h7>Use this test to test for the variance or standard deviation of your sample.
<br>
<br>Example:
<br>On the average, is the amount of product dispensed by the machine consistent with less than 20g of deviation?</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p72" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>The Statistical Test Selector does not yet include a test for one variance from a non-normal population.
                </h6>
                    <h7></h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p73" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Wilcoxon Matched-Pairs Signed-Rank Test for Median
<sup>[<a href="https://courses.washington.edu/psy524a/_book/nonparametric-tests.html#wilcoxons-matched-pairs-signed-ranks-test" target = "_blank" title="Wilcoxon Signed-Ranks Test">2</a>]</sup>                    </h6>
                    <h7>Use this test for testing the median of paired differences, or as an alternative to Dependent Samples t-Test when the normality assumption is violated.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p75" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Wilcoxon&#39;s Rank-Sum Test
<sup>[<a href="https://courses.washington.edu/psy524a/_book/nonparametric-tests.html#wilcoxons-rank-sum-test" target = "_blank" title="Wilcoxon&#39;s Rank-Sum Test">2</a>]</sup>                    </h6>
                    <h7>Use this test for testing the difference in medians of two populations, or as an alternative to Independent Samples t-Test when the one of the populations is not normally distributed.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p76" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>The Statistical Test Selector does not yet include a test for paired samples difference in variances.
                </h6>
                    <h7></h7>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p77" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Are the groups both normally distributed?
                </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a77" data-target="p78" data-source="p77">
                            Yes
                        </button>
                        <button class="answer btn btn-primary" id="a78" data-target="p79" data-source="p77">
                            No
                        </button>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p78" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>F-test on Two Population Variances
<sup>[<a href="https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Introductory_Statistics_1e_(OpenStax)/13%3A_F_Distribution_and_One-Way_ANOVA/13.05%3A_Test_of_Two_Variances" target = "_blank" title="F-Test">2</a>]</sup>                    </h6>
                    <h7>Use this test when you want to test for difference between two variances from different normal distributions.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p79" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>The Statistical Test Selector does not yet have a test for difference in variances from non-normal populations.
                </h6>
                    <h7></h7>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p80" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Which of the following pairs best describe your variables?
                </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a80" data-target="p81" data-source="p80">
                            One Ordinal, One Interval/Ratio
                        </button>
                        <button class="answer btn btn-primary" id="a81" data-target="p82" data-source="p80">
                            Both Interval/Ratio
                        </button>
                        <button class="answer btn btn-primary" id="a82" data-target="p83" data-source="p80">
                            Other
                        </button>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p81" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Spearman&#39;s Rank Correlation
<sup>[<a href="https://mathcenter.oxford.emory.edu/site/math117/rankCorrelation/" target = "_blank" title="Spearman&#39;s Rank">2</a>]</sup>                    </h6>
                    <h7>Use this test when your data is ranked, or as an alternative when the assumptions of Pearson's Correlation is violated.</h7>
            </div>
        </div>
        <div class="bg-light border border-1 container-xxl prompt rounded-3 visually-hidden" id="p82" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Are you willing to assume that the variables have a bivariate normal distribution?
<sup>[<a href="https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/05%3A_Special_Distributions/5.07%3A_The_Multivariate_Normal_Distribution" target = "_blank" title="Bivariate Normal Distribution">2</a>]</sup>                    </h6>
            </div>
            <div class="container-fluid" style="padding:5px">
                        <button class="answer btn btn-primary" id="a83" data-target="p84" data-source="p82">
                            Yes
                        </button>
                        <button class="answer btn btn-primary" id="a84" data-target="p85" data-source="p82">
                            No
                        </button>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p83" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>The Statistical Test Selector does not yet include a test for this selection.
                </h6>
                    <h7></h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p84" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>Pearson&#39;s Correlation
<sup>[<a href="https://stats.libretexts.org/Bookshelves/Applied_Statistics/Basic_Statistics_Using_R_for_Crime_Analysis_(Choi)/01%3A_Chapters/1.09%3A_Correlation" target = "_blank" title="Pearson&#39;s Correlation">3</a>]</sup>                    </h6>
                    <h7>Use this test to test for the linear relationship between two continuous variables.</h7>
            </div>
        </div>
        <div class="bg-info-subtle border border-1 container-xxl prompt rounded-3 visually-hidden" id="p85" style="padding: 10px; margin-bottom: 10px">
            <div class="container" style="padding-bottom: 5px">
                <h6>The Statistical Test Selector does not yet include a test for this selection.
<sup>[<a href="https://mathcenter.oxford.emory.edu/site/math117/rankCorrelation/" target = "_blank" title="Alternative: Spearman&#39;s Correlation">alt</a>]</sup>                    </h6>
                    <h7>Recommendation: Transform the data into ranks and use Spearman's Rank Correlation for your analysis.</h7>
            </div>
        </div>
    </div>
    <button class="answer btn btn-light" id="undoButton" disabled>
        Undo
    </button>
    <button class="answer btn btn-light" id="resetAns" disabled>
        Reset Answers
    </button>
</div>
    <!-- Script 1: Remove hidden from first question -->
    <script>
        const pOne = document.getElementById("p1");
        pOne.classList.remove("visually-hidden");
    </script>

    <!-- Script 2: Add an activator to the answers -->
    <!-- Script 4: Undo Button-->
    <script>
        var currentPrompt = pOne;
        var previousPrompt;
        var previousPeers;
        const options = document.querySelectorAll(".answer");
        const undoButton = document.querySelector("#undoButton");
        const resetAnsButton = document.querySelector("#resetAns");
        // what happens when the undo button is clicked
        function setCurrentPrompt(cp, pp) {
            currentPrompt = cp;
            previousPrompt = pp;
            previousPeers = document.querySelectorAll("button[data-source=" + pp.id + "]");
        }
        function undofxn() {
            var newpreviousid;
            // the current prompt is hidden
            currentPrompt.classList.add("visually-hidden");
            // the previous prompt options are no longer disabled
            for (peer of previousPeers) {
                peer.removeAttribute("disabled");
                peer.classList.remove("btn-outline-primary");
                peer.classList.add("btn-primary");
                oneid = document.querySelector("button[data-target=" + previousPrompt.id + "]")
            }
            if (oneid === null) {
                undoButton.setAttribute("disabled","disabled")
                resetAnsButton.setAttribute("disabled","disabled")
            }
            else {
                newpreviousid = document.getElementById(oneid.getAttribute("data-source"));
                setCurrentPrompt(previousPrompt, newpreviousid);
            }
        }
        function setUndo(cp) {
            undoButton.removeEventListener('click', undofxn);
            undoButton.addEventListener('click', undofxn);
        }
        undoButton.addEventListener('click', undofxn);
        for (opt of options) {
            // target is a prompt
            let target = document.getElementById(opt.getAttribute("data-target"));
            // source is a prompt
            let source = document.getElementById(opt.getAttribute("data-source"));
            // peers are buttons
            let peers = document.querySelectorAll("button[data-source=" + opt.getAttribute("data-source") + "]")
            let my_id = opt.id
            opt.addEventListener('click', () => {
                if (target === null) {}
                else {
                    undoButton.removeAttribute("disabled");
                    resetAnsButton.removeAttribute("disabled");
                    target.classList.remove("visually-hidden");
                    for (peer of peers) {
                        if (!(peer.id === my_id)) {
                            peer.setAttribute("disabled", "disabled");
                            peer.classList.remove("btn-primary");
                            peer.classList.add("btn-outline-primary");
                        }
                        else {
                            peer.setAttribute("disabled", "disabled");
                        }
                    };
                    setCurrentPrompt(target, source);
                    setUndo(target);
                }
            });
        };
    </script>

    <!-- Script 3: Add Reset Answers button without refreshing page-->
    <script>
        const prompts = document.querySelectorAll(".prompt");
        resetAnsButton.addEventListener('click', () => {
            for (opt of options) {
                opt.removeAttribute("disabled");
                opt.classList.remove("btn-outline-primary");
                opt.classList.add("btn-primary");
            }
            for (prompt of prompts) {
                prompt.classList.add("visually-hidden");
            }
            pOne.classList.remove("visually-hidden");
            undoButton.setAttribute("disabled", "disabled");
            resetAnsButton.setAttribute("disabled", "disabled");
        })
    </script>
    </main>
    <!-- About Us Modal-->
    <div class="modal fade" id="AboutUs" tabindex="-1" aria-labelledby="AboutUsLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="AboutUsLabel">About DIY Stats</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <!-- <h6> -->
                        <p>DIY Stats is an passion project of Rocket Scientist Teachers to design web applications for statistical needs.</p>
                        <p>Currently, we are working on a Statistical Test Selector so students in research are able to navigate the many
                        different statistical tests simply by answering a series of questions.</p>
                        <p>In the future, Rocket Scientist Teachers plan to develop even more web applications for other statistical concepts.</p>
                    <!-- </h6> -->
                </div>
            </div>
        </div>
    </div>
    <!-- Contact Us Modal-->
    <div class="modal fade" id="ContactUs" tabindex="-1" aria-labelledby="ContactUsLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="ContactUsLabel">Rocket Scientist Teachers</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <h6>
                        <p>LinkedIn:</p>
                        <p>Gmail:</p>
                        <p>Facebook:</p>
                    </h6>
                </div>
                <div class="modal-footer">
                        <p>Web Developer/Junior Statistician: <a href="/cvitae" target = "_blank">duriandritz</a></p>
                </div>
            </div>
        </div>
    </div>

</body>