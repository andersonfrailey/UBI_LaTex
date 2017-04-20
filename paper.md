\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{tabularx}
\usepackage{rotating}
\usepackage{booktabs}
\usepackage{authblk}
\usepackage{amsthm}
\usepackage{amssymb}
\usepackage{amsmath}
\usepackage[margin=2.5cm]{geometry}
\usepackage{setspace}
\usepackage{graphicx}
\usepackage{enumerate}
\usepackage{caption}
\usepackage{adjustbox}
\usepackage{indentfirst}
\captionsetup[figure]{
   position=above,
}
\usepackage[capposition=top]{floatrow}
%\usepackage[hidelinks]{hyperref}
\usepackage{hyperref}
\usepackage{xcolor}
\hypersetup{
	colorlinks={true},
	linkcolor={blue!50!black},
	citecolor={black!50!black},
	urlcolor={black!80!black}
}

% Bib Code
%\usepackage[style=authoryear-ibid,sorting=ynt]{biblatex}
%\usepackage[backend=biber]{biblatex}
\begin{document}
% define macros
\input{macros.txt}

\newcommand{\ospc}{\footnote{Author’s calculations using OSPC Tax-Calculator.}}

%\begin{document}
\begin{titlepage}

\title{Universal Basic Income Reform}
\author{Open Source Policy Center \\ American Enterprise Institute}
\date{\today}

\maketitle

\end{titlepage}

\tableofcontents
\newpage

\doublespacing

% Section 1
\section{Introduction}

Widening inequality and increasing job disruption due to technology have increased discussion of an universal basic income (UBI) in academic circles. The concept of an UBI is simple -- every person, above a certain age, receives a lump sum of cash from the government regardless of income, employment status, or any other requirement typically used in welfare programs. Using the American Enterprise Institute's Open Source Policy Center's (OSPC) modeling suite, this report simulates the repeal of major welfare and transfer programs, the elimination of tax provisions and deductions to broaden the tax base, and three potential UBI policies that would neutralize the revenue impact of the aforementioned reforms on a static and dynamic basis. The paper also evaluates the welfare consequences of these reforms, accounting for the inefficiency costs of welfare programs. Analysis is performed by separating tax units by percentiles of average gross income (AGI). All calculations are performed using 2014 data.

% Section 2
\section{Welfare/Transfer Program Repeal}
We begin by repealing all major welfare and transfer programs including Medicare, Medicaid, SSI, SNAP, Social Security, and Veterans Benefits.\footnote{Program payments imputed using OSPC C-TAM model. A full description of the model can be found in the appendix.} We also repealed unemployment, housing, and student assistance; other public assistance; and most individual payment programs.\footnote{A full list of the programs repealed and their costs can be found in the appendix.} We account for decreased tax revenue from the repeal of Social Security benefits, which are taxed under the current system. Afeter accounting for the decrease in tax revenue from the repeal of taxable Social Security benefits, repealing these programs yields \$\axag{}trillion in funds that can be used to put toward the UBI.\footnote{Author's calculations using C-TAM, Tax-Calculator, and \href{https://obamawhitehouse.archives.gov/omb/budget/Historicals}{Office of Management and Budget data (\textit{Table 3.2—Outlays by Function and Subfunction: 1962–2021} and \textit{Table 11.3—Outlays for Payments for Individuals by Category and Major Program: 1940–2021).}}} The effects of repealing the welfare and transfer programs are shown in the following table. 

\begin{table}[H]
\caption{Welfare and Transfer Program Repeal Effect on Benefits}
\begin{center}
\begin{adjustbox}{max width=\textwidth}
\input{a1_df.txt}
\end{adjustbox}
\end{center}
\floatfoot{Source: Author's calculations using OSPC calculator.}
\end{table}

The repeal of benefit and transfer programs appears to have a homogenous effect across AGI percentiles due to the inclusion of Social Security and Medicaid.\footnote{As a result of these reforms, the bottom $20$ percent of income earners lose $20.47$ percent of the benefits, while the top $20$ percent of earners lose $23.74$ percent of the benefits.} Social Security disbursments are tied to an individual's income, compensating for the larger recipt of other benefit and transfer programs by low income earners.
\footnote{C-TAM only models Medicare, Medicaid, SSI, SNAP, Social Security, and Veterans Benefits. The distribution of all non-modeled programs was assumed to reflect the distribution of the modeled benefits.}

\begin{figure}[H]
%\centering
\begin{center}
\caption{Average Benefit Change by Percentile of AGI}
\includegraphics[scale=0.650]{a1}
\end{center}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Total Benefit Change by Percentile of AGI}
\includegraphics[scale=0.650]{a2}
%\floatfoot{A note}
\end{figure}

These reforms have similar tax effects for both primary and secondary earners, raising the marginal tax rate (MTR) for those with lower income and lowering the MTR for those with middle incomes. The MTRs of those with higher incomes are reletively unaffected by the repeal of welfare and transfer programs. One benefit of the reforms is it removes the disincentive to work associated with welfare "notches." These form when the MTR is such that the additional income from an extra dollar earned through work will result in the loss of significant welfare benefits.

% Section 3
\section{Tax Reform}
The current tax code is littered with numerous exemptions and deductions designed to give certain segments of the population tax breaks. These provisions narrow the tax base, distort tax unit consumption decisions, and have disperate effects across the income distribution.  In addition to repealing all welfare and transfer programs, we repeal all above-the-line, standard, and itemized deductions (excluding the charitable deduction); all tax credits; the personal exemption; and the earned income tax credit.

With the repeal of the aforementioned tax provisions, roughly $92$ percent of tax units will face a tax increase resulting in $\$708$ billion in new liabilities, nearly half of that falling on the top twenty percent of earners -- $49.01$ percent -- compared to the $3.68$ percent borne by the bottom twenty percent.\footnote{Author’s calculations using OSPC Tax-Calculator.}

\begin{table}[H]
\caption{Tax Liability by Percentile of AGI}
\begin{center}
\begin{adjustbox}{max width=\textwidth}
\input{b1_df.txt}
\end{adjustbox}
\end{center}
\floatfoot{Source: Author's calculations using OSPC calculator.}
\end{table}

\begin{figure}[H]
\centering
\caption{Average Tax Liability by Percentile of AGI}
\includegraphics[scale=0.650]{b1}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Total Tax Liability by Percentile of AGI}
\includegraphics[scale=0.650]{b2}
%\floatfoot{A note}
\end{figure}

The reforms lead to almost across the board marginal tax rate (MTR) increases, the largest of which are seen at the lower end of the income spectrum. The bottom quarter of earners see their marginal net-of-tax rate $(1 - MTR)$ decrease by 17 percentage points for both primary and secondary earners.\footnote{Author’s calculations using OSPC Tax-Calculator.}


\begin{figure}[H]
\centering
\caption{Average Primary Earner MTR by Percentile}
\includegraphics[scale=0.650]{b3}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Average Secondary Earner MTR by Percentile}
\includegraphics[scale=0.650]{b4}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Average Pct. Change in (1-MTR) by Percentile}
\includegraphics[scale=0.650]{b5}
%\floatfoot{A note}
\end{figure}

% Section 4
\section{Tax and Welfare/Transfer Repeal}

This section combines the welfare and transfer repeal from section two and tax reform from section three to examine the joint distributional impact. The top ten percent of earners see an average negative impact of just over $\$30,000$ compared to slightly more than $\$15,000$ in the bottom ten percent. The top $20$ percent experiences $30.21$ percent of the increase in tax liabilities, while the lowest $20$ percent pay $16.28$ percent of the increase in tax liabilities (Question: is this supposed to refer to the % of the negative impact rather than the tax liabilities?-Anderson). 

\begin{table}[H]
\caption{Revenue Effect of Benefit and Tax Repeal}
\begin{center}
\begin{adjustbox}{max width=\textwidth}
\input{c1_df.txt}
\end{adjustbox}
\end{center}
\floatfoot{Source: Author's calculations using OSPC calculator.}
\end{table}

Combined, reforming the tax code to remove deductions, exemptions, and other provisions that narrow the base as well as repealing most programs that distribute payment to individuals freed $\$2.9$ trillion to apply to a UBI.

\begin{figure}[H]
\centering
\caption{Average Revenue Effect of Benefit and Tax Repeal by Percentile of AGI}
\includegraphics[scale=0.650]{c1}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Total Revenue Effect of Benefit and Tax Repeal by Percentile of AGI}
\includegraphics[scale=0.650]{c2}
%\floatfoot{A note}
\end{figure}

% the following tables DO NOT EXIST as of 4-11-2017
%\begin{figure}[H]
%\centering
%\caption{Average Primary Earner MTR by Percentileof AGI}
%\includegraphics[scale=0.650]{c3}
%\floatfoot{A note}
%\end{figure}

%\begin{figure}[H]
%\centering
%\caption{Average Secondary Earner MTR by Percentile of AGI}
%\includegraphics[scale=0.650]{c4}
%\floatfoot{A note}
%\end{figure}

% Section 5
\section{Tax and Welfare/Transfer Repeal with UBI for All}

The first UBI policy modeled provides a UBI to all individuals with those under the age of eighteen receiving half of what those above do. We programmed the model to set a UBI that would be revenue neutral after accounting for all of the reforms in section four and the new tax revenue that results from making the UBI taxable. We found that we could achieve revenue neutrality with a UBI of \$\dxaa{}for those above the age of 18 and \$\dxab{}for those under the age of 18.\ospc The effect of this policy on tax liabilities can be see in table \ref{table:d1}.  

\begin{table}[H]
\caption{Increase in Tax Liabilities by Percentile of AGI}
\label{table:d1}
\begin{center}
\begin{adjustbox}{max width=\textwidth}
\input{d1_df.txt}
\end{adjustbox}
\end{center}
\floatfoot{Source: Author's calculations using OSPC calculator.}
\end{table}

The combination of repealing tax deductions and exemptions which lower tax liability and taxing the UBI results in greater tax liabilities for all income earners. The UBI alone moves all non-head-of-household filers from the $10$ to the $15$ percent tax bracket. Total increased tax liabilities of $\$1.36$ trillion are paid largely by high income earners. The bottom $20$ percent pays $9.66$ percent of the increased tax liabilities while the top $20$ percent pays $41.71$ percent of the increased tax liabilities. 

There are a handful of tax-units who do see a tax cut: this is due to the repeal of the Social Security and therefore taxable Social Security income. Of the tax-units receiving a tax cut, less than one tenth of one percent of all units, their average Social Security income before repeal was $\$38,407$, compared to an average UBI benefit of $\$16,180$.


\begin{figure}[H]
\centering
\caption{Average Primary Earner MTR by Percentile of AGI}
\includegraphics[scale=0.650]{d3}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Average Secondary Earner MTR by Percentile of AGI}
\includegraphics[scale=0.650]{d4}
%\floatfoot{A note}
\end{figure}

Those in the lower spectrum of earners see their net-of-tax rate drop by as nineteen percent after the reforms and UBI are accounted for.

As a whole, the tax effects of a UBI are largely progressive, with the top twenty percent of earners shouldering over forty percent of the increase in liabilities.

\begin{figure}[H]
\centering
\caption{Average Change in Tax Liabilities by Percentile of AGI}
\includegraphics[scale=0.650]{d1}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Total Change in Tax Liabilities by Percentile of AGI}
\includegraphics[scale=0.650]{d2}
%\floatfoot{A note}
\end{figure}

Because everyone, regardless of age, receives a basic income, this policy is most friendly to families with children of our three simulated options, one of which excludes anyone under eighteen and the other all those under twenty-one.

\begin{figure}[H]
\centering
\caption{Average Pct. Change in (1-MTR) by Percentile}
\includegraphics[scale=0.650]{d5}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Average Pct. Change in (1-MTR) by Percentile}
\includegraphics[scale=0.650]{d5}
%\floatfoot{A note}
\end{figure}

% Section 6
\section{Tax and Welfare/Transfer Repeal with UBI for 18 Plus}
In this section we provide a basic income to individuals $18$ and older. Shrinking the targeted population allows for a larger UBI -- \$\exaa{}instead of the \$\dxaa{} outlined in section five.\ospc As in section five, this UBI is taxed and is ultimatley revenue neutral.

With the introduction of a \$\exaa{}UBI, most tax units see a rise in tax liability and marginal tax rates. As with the initial UBI policy though, there are a small number of tax-units who actually saw their total liability decrease $\$1,436$ on average. This is again likely due to the removal of taxable Social Security benefits from these tax units, as on average they received $\$41,117$ compared to $\$18,611$ in UBI.\ospc

\begin{figure}[H]
\centering
\caption{Average Primary Earner MTR by Percentile of AGI}
\includegraphics[scale=0.650]{e3}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Average Secondary Earner MTR by Percentile of AGI}
\includegraphics[scale=0.650]{e4}
%\floatfoot{A note}
\end{figure}

As with our first UBI policy, the largest changes in marginal tax rates are seen in the lower end of the income spectrum as those who earn the least are pushed into higher tax brackets by the UBI and tax benefits from the standard deduction and personal exemptions are removed.

\begin{table}[H]
\caption{Increase in Tax Liabilities by Percentile of AGI}
\begin{center}
\begin{adjustbox}{max width=\textwidth}
\input{e1_df.txt}
\end{adjustbox}
\end{center}
\floatfoot{Source: Author's calculations using OSPC calculator.}
\end{table}

\begin{figure}[H]
\centering
\caption{Average Change in Tax Liabilities by Percentile of AGI}
\includegraphics[scale=0.650]{e1}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Total Change in Tax Liabilities by Percentile of AGI}
\includegraphics[scale=0.650]{e2}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Average Pct. Change in (1-MTR) by Percentile}
\includegraphics[scale=0.650]{e5}
%\floatfoot{A note}
\end{figure}

In dollar terms, most of the new tax burden still falls on the shoulders of higher earners. Those in the top ten percent would be responsible for more than a quarter of new liabilities compared to the three percent increase in the bottom percentile.

% Section 7
\section{Tax and Welfare/Transfer Repeal with UBI for 21 Plus}
This section impliments a UBI limited to those 21 and above. Using the goal of revenue neutrality after accounting for taxes on the additional income, we found that a UBI of \$\fxaa{} could be given to all 21 and above.

Unlike when the UBI was given to all above $18$, the additional tax liabilities offset any drop in liabilities resulting from the loss of taxable benefits, so no tax units see a cut in taxes. As with the previously discussed reforms, the progressivity of the tax effects is still maintained despite large marginal tax rate increases in the bottom percentiles.

\begin{table}[H]
\caption{Tax Liability by Percentile of AGI}

\begin{center}
\begin{adjustbox}{max width=\textwidth}
\input{f1_df.txt}
\end{adjustbox}
\end{center}
\floatfoot{Source: Author's calculations using OSPC calculator.}
\end{table}

\begin{figure}[H]
\centering
\caption{Average Change in Tax Liabilities by Percentile of AGI}
\includegraphics[scale=0.650]{f1}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Total Change in Tax Liabilities by Percentile of AGI}
\includegraphics[scale=0.650]{f2}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Average Primary Earner MTR by Percentileof AGI}
\includegraphics[scale=0.650]{f3}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Average Secondary Earner MTR by Percentile of AGI}
\includegraphics[scale=0.650]{f4}
%\floatfoot{A note}
\end{figurf}

\begin{figure}[H]
\centering
\caption{Average Pct. Change in (1-MTR) by Percentile}
\includegraphics[scale=0.650]{f5}
%\floatfoot{A note}
\end{figure}

% Section 8
\section{Tax and Welfare/Transfer Repeal with UBI for All (Dynamic)}
To this point, we have assumed no change in behavior stemming from either tax reform or UBI implementation. Using Tax-Calculator’s behavioral analysis capabilities, we repeated simulations of the three UBI policies above, this time applying an income effect of $-0.05$ and a substitution effect of $0.24$.\footnote{Our elasticities are based on Harris (2015). Both the tax reform package and UBI policies specified in this paper increase marginal and average tax rates. By itself, the substitution effect dictates this result in a decrease in the labor supply, while the offsetting income effect implies an increase in labor supply.} This allows for dynamic responses to labor and leisure choices made by UBI recipients. 

\begin{table}[H]
\caption{Tax Liability by Percentile of AGI}
\begin{center}
\begin{adjustbox}{max width=\textwidth}
\input{g1_df.txt}
\end{adjustbox}
\end{center}
\floatfoot{Source: Author's calculations using OSPC calculator.}
\end{table}

\begin{figure}[H]
\centering
\caption{Average Change in Tax Liabilities by Percentile of AGI}
\includegraphics[scale=0.650]{g1}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Total Change in Tax Liabilities by Percentile of AGI}
\includegraphics[scale=0.650]{g2}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Average Primary Earner MTR by Percentileof AGI}
\includegraphics[scale=0.650]{g3}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Average Secondary Earner MTR by Percentile of AGI}
\includegraphics[scale=0.650]{g4}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Average Pct. Change in (1-MTR) by Percentile}
\includegraphics[scale=0.650]{g5}
%\floatfoot{A note}
\end{figure}

% Section 9
\section{Tax and Welfare/Transfer Repeal with UBI for 18 Plus (Dynamic)}
This section implements a taxable UBI of \$\hxaa{}for individuals at least $18$ years and performs a dynamic simulation. Increases in tax liability are similar in both static and dynamic simulations: the static simulation raises total tax liabilities by $\$1.364$ trillion while the dynamic simulation raises tax liabilities by $\$1.371$ trillion. Of this increase in tax liability, $26.09$ percent is borne by those in the highest AGI percentile. Those in the lowest AGI percentile only face $3.66$ percent of the total increase in tax liability. This amounts to an average $\$3,081$ increase for tax units in the lowest income percentile. The following table shows the complete impact of these reforms on liability by AGI percentile.

\begin{table}[H]
\caption{Tax Liability by Percentile of AGI}
\begin{center}
\begin{adjustbox}{max width=\textwidth}
\input{h1_df.txt}
\end{adjustbox}
\end{center}
\floatfoot{Source: Author's calculations using OSPC calculator.}
\end{table}

The impact of these reforms on tax liability are also shown in the following bar charts. The first shows the average increase in tax liability by AGI percentile, while the second shows the total increase in tax liability by AGI percentile.

\begin{figure}[H]
\centering
\caption{Average Change in Tax Liabilities by Percentile of AGI}
\includegraphics[scale=0.650]{h1}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Total Change in Tax Liabilities by Percentile of AGI}
\includegraphics[scale=0.650]{h2}
%\floatfoot{A note}
\end{figure}

These reforms have a regressive impact on the MTR, raising it for low and medium income earners while leaving it largely unchanged for high income earners. This results in an increase in the MTR of approximately $10$ percentage points for primary income earners in the l lowest two income percentiles. Primary earners with medium incomes experience an average increase in the MTR of approximately $5$ percentage points. Secondary income earners experience an even larger increase in MTR, with an increase of $20$ percentage points for the lowest two income percentiles and an increase of approximately $10$ percentage points for those with medium incomes. Those in the $30\%$ to $40\%$ income percentile see little change in their MTR, as the baseline rapidly increases for these individuals. These results are illustrated in the following charts. 

\begin{figure}[H]
\centering
\caption{Average Primary Earner MTR Change by Percentile of AGI}
\includegraphics[scale=0.650]{h3}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Average Secondary Earner MTR Change by Percentile of AGI}
\includegraphics[scale=0.650]{h4}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Average Pct. Change in (1-MTR) by Percentile}
\includegraphics[scale=0.650]{h5}
%\floatfoot{A note}
\end{figure}

% Section 10
\section{Tax and Welfare/Transfer Repeal with UBI for 21 Plus (Dynamic)}
This section implements a taxable UBI of $\$12,126$ for those $21$ years of age and performs a dynamic simulation. These reforms increased total tax liabilities by $\$1.375$ trillion. The increase in tax liability is largest for those with the highest incomes. Of the total increase in tax liabilities, $26.21$ percent are paid by those in the top income percentile. Those with the lowest incomes face a comparatively smaller increase in the tax liability, accounting for $3.45$ percent of the total increase in tax liabilities. This equates to an average increase in $\$2,914$ for those with the lowest incomes. The following table shows complete results.

\begin{table}[H]
\caption{Change in Tax Liabilities by Percentile of AGI}

\begin{center}
\begin{adjustbox}{max width=\textwidth}
\input{i1_df.txt}
\end{adjustbox}
\end{center}
\floatfoot{Source: Author's calculations using OSPC calculator.}
\end{table}

The impact of these reforms on tax liabilities are also illustrated in the following charts. The wealthiest have substantially higher average and total tax liabilities under reform.

\begin{figure}[H]
\centering
\caption{Average Change in Tax Liabilities by Percentile of AGI}
\includegraphics[scale=0.650]{i1}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Total Change in Tax Liabilities by Percentile of AGI}
\includegraphics[scale=0.650]{i2}
%\floatfoot{A note}
\end{figure}

These reforms substantially raise the MTR for low and medium earners while the MTR for high income earners are largely unaffected.
Primary earners with low incomes experience a large increase in MTR of between $10$ and $5$ percentage points. Those in the highest income percentile see little to no change in their MTR. Secondary income earners experience similar effects as those seen in the UBI $18$ plus dynamic simulation, with those in the first two income percentiles experiencing a $20$ percentage point MTR increase. Those in the $30\%$ to $40\%$ income percentile range experience little change in their MTR. Those with middle incomes experience $10$ percentage point increases in MTR rates.

\begin{figure}[H]
\centering
\caption{Average Primary Earner MTR Change by Percentileof AGI}
\includegraphics[scale=0.650]{i3}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Average Secondary Earner MTR Change by Percentile of AGI}
\includegraphics[scale=0.650]{i4}
%\floatfoot{A note}
\end{figure}

\begin{figure}[H]
\centering
\caption{Average Pct. Change in (1-MTR) by Percentile}
\includegraphics[scale=0.650]{i5}
%\floatfoot{A note}
\end{figure}

% Section 11
\section{Adjusted Welfare Calculations}
This section evaluates the welfare effects of a UBI -- all using dollar-welfare and adjusted baseline welfare calculations. A dollar-welfare measure sets the value of a welfare or transfer program per tax unit equal to the average cost. This method is inaccurate if the recipients do not receive a benefit worth the program’s per capita cost due to deadweight loss.\footnote{ O'Higgins (1981) provides the example of educational benefits, which when measured using the cost per capita method inflates if teachers received increased wages. This leads to a higher estimated value to students, despite the wage increase having no actual impact on education provision. The corollary can also be true when economies of scale are considered: a government may be able to purchase a good or service in bulk and demand a lower price, despite the services being valued more. To avoid these problems, in-kind health care provision should be valued, using a risk-related insurance approach. Individuals are assigned a dollar benefit (the actuarily fair premium price) based upon average spending according to their age and sex. Callan (2008) explains that consumption of health services is not considered, as this would suggest those most sick and in need of medical treatment have greater resources. Smeeding (1993) writes that the average cost of the benefit may overstate it, as recipients may prefer to spend corresponding cash on other goods and services.} The size of the deadweight loss depends on the recipient’s infra-marginality with respect to the program’s benefit. If the recipient is infra-marginal, meaning they will spend more than a given program’s benefit on a good or service, there is little to no welfare loss. In this case, the benefit recipient is going to spend at least as much as the welfare program provides, leaving them to make marginal consumption decisions. If the value of the program exceeds the amount the recipient would pay for a good or service (the recipient is not infra-marginal), a deadweight loss results from the recipient consuming more than they otherwise would. In this case, the recipient would be better off with cash for the value of the benefit exceeding their desired consumption level.\footnote{Example: A household receives a heating fuel subsidy for an amount in excess of their desired heating fuel consumption. The household is best off consuming the maximum amount of heating fuel provided by the program although they may be better off restricting their consumption and receiving the remainder of the subsidy in cash (which they could spend on other goods).} This deadweight loss is partially offset by the improved targeting of beneficiaries.

To account for these deadweight losses, we employ welfare multiples that can be applied to each dollar spent on a specific program to approximate the value to recipients. These multiples are derived from the literature when availible, or approximated using simmilar programs.\footnote{See the appendix for a table of welfare multiples from the literature.} These multiples allow for a more accurate calculation of welfare programs' benefits to individuals.

The welfare multiples used in this section are shown in the following table.

%\begin{table}[H]
%\caption{Welfare Multiples by Program}
%\begin{center}
%\begin{adjustbox}{max width=\textwidth}
%\begin{tabular}{lr}
%\toprule
%Program 		&  Welfare Multiple	\\
%\midrule
%Medicaid 		&	0.30	\\		
%Medicare 		&	0.75	\\
%SNAP 			&	0.95	\\
%Social Security &	0.95	\\
%SSI				&	0.99	\\
%Veterans' Benefits & 0.95	\\
%\bottomrule
%\end{tabular}
%\end{adjustbox}
%\end{center}
%\floatfoot{Source: Literature and author's calculations.}
%\end{table}

\begin{table}[H]
\caption{Welfare Multiples by Program}
\begin{center}
\begin{adjustbox}{max width=\textwidth}
\input{j1_df.txt}
\end{adjustbox}
\end{center}
\floatfoot{Source: Literature and author's calculations.}
\end{table}

The welfare multiples are applied to the dollar value of each transfer program per tax unit. These are then aggregated by percentile of AGI to evaluate the distributional effects of repealing all welfare and transfer programs and implementing a UBI. We assume that the UBI will produce little to no deadweight loss because it is a cash transfer without any means testing. These welfare multiples only account for deadweight losses in the programs themselves and not for any tax effects.\footnote{We hope to include the welfare effects of the tax deduction and exemption repeals in later editions of this paper.}

The following tables and charts illustrate the distributional effects of a UBI for all, accounting for the deadweight loss present in the welfare programs. Compared to the pure dollar-welfare calculation, the adjusted welfare calculation finds $\$5,000$ less in welfare for those in the lowest income percentile.

\begin{table}[H]
\caption{Dollar Welfare and Adjusted Welfare Calculations}
\begin{center}
\begin{adjustbox}{max width=\textwidth}
\input{j2_df.txt}
\end{adjustbox}
\end{center}
%\floatfoot{Source: Literature and author's calculations.}
\end{table}

The following table shows the average and total welfare resulting from repealing welfare and transfer programs, repealing tax exemptions and deductions, and implimenting a UBI. In all situations, those in the lowest income percentile experience a welfare loss, while those in the lower-to-middle income percentiles experience a welfare gain. 


\begin{table}[H]
\caption{Average Welfare by Percentile}
\begin{center}
\begin{adjustbox}{max width=\textwidth}
\input{j6_df.txt}
\end{adjustbox}
\end{center}
%\floatfoot{Source: Literature and author's calculations.}
\end{table}


\begin{table}[H]
\caption{Total Welfare by Percentile}
\begin{center}
\begin{adjustbox}{max width=\textwidth}
\input{j7_df.txt}
\end{adjustbox}
\end{center}
%\floatfoot{Source: Literature and author's calculations.}
\end{table}

The following bar chart illustrates the welfare effects of implementing a range of UBI schemes, compared with the baseline dollar-welfare and adjusted welfare calculations. When viewed against the dollar-welfare calculation, the UBI for all does not increase welfare for the lowest income percentile. However, when this is compared with the adjusted welfare calculation, the UBI does result in increased welfare.  

\begin{figure}[H]
\centering
\caption{Welfare Effects of UBI}
\includegraphics[scale=0.650]{j1}
\floatfoot{Welfare only includes government transfer and transfer programs.}
\end{figure}

%\section{Conclusion}

%More work must be done to examine the disincentive effects of the UBI %combined with high marginal tax rates for low income earners. They %may be more likely to sit out of the workforce and not engage in low %income work given the UBI's fixed income and higher MTR.

\newpage
\begin{thebibliography}{1}

\bibitem{bib01} Author, \textit{Title}, publisher, location, year.

\bibitem{bib02} Office of Management and Budget, \textit{Table 3.2—Outlays by Function and Subfunction: 1962–2021}.\\ \texttt{https://obamawhitehouse.archives.gov/omb/budget/Historicals}

\bibitem{bib03} Office of Management and Budget, \textit{Table 11.3—Outlays for Payments for Individuals by Category and Major Program: 1940–2021}.\\ \texttt{https://obamawhitehouse.archives.gov/omb/budget/Historicals}

\bibitem{bib04} Veterans Benefits Administration, \textit{Annual Benefits Report: Fiscal Year 2014}.\\ \texttt{http://www.benefits.va.gov/REPORTS/abr/ABR-IntroAppendix-FY14-11032015.pdf}.

\bibitem{bib05} Veterans Benefits Administration, \textit{Annual Benefits Report: Compensation}.\\ \texttt{http://www.benefits.va.gov/REPORTS/abr/ABR-Compensation-FY14-10202015.pdf}

\bibitem{bib06} Angrist, Joshua D, “The Effect of Veterans Benefits on Education and Earnings.” \textit{ILR Review}. Vol. 46, No. 4 (Jul., 1993), pp. 637-652.\\ \texttt{http://www.jstor.org/stable/2524309}

\bibitem{bib07} O'Higgins, Michael and Patricia Ruggles, "The Distribution of Public Expenditures and Taxes Among Households in the United Kingdom." \textit{Review of Income and Wealth}. Vol. 27, No. 3. (1981), pp. 298-326.\\ \texttt{http://onlinelibrary.wiley.com/doi/10.1111/j.1475-4991.1981.tb00207.x/full}

\bibitem{bib08} Callan, Tim and Claire Keane, "Non-cash Benefits and the Distribution of Economic Welfare." \textit{Economic and Social Review}. Vol. 40, No. 1. (2008), pp. 49-71.\\ \texttt{http://ftp.iza.org/dp3954.pdf} 

\bibitem{bib09} Smeeding, Timothy M. and Peter Saunders, John Coder, Stephen Jenkins, Johan Fritzell, Aldi J. M. Hagenaars, Richard Hauser, and Michael Wolfson. "Poverty, Inequality, and Family Living Standards Impacts Across Seven Nations: The Effect of Noncash Subsidies for Health, Education and Housing." \textit{Review of Income and Wealth}. Vol. 39, No. 3. (1993), pp. 229-256.\\ \texttt{http://www.roiw.org/1993/229.pdf}

\bibitem{bib10} Harris, Edward and Shannon Mok, "How CBO Estimates the Effects of the Affordable Care Act on the Labor Market." Congressional Budget Office. Working Paper 2015-09 (December, 2015).\\ \texttt{https://www.cbo.gov/publication/51065}

\end{thebibliography}
 
\newpage
\section{Appendix}

\subsection{OSPC's Tax Calculator}
OSPC’s Tax-Calculator is an open source microsimulation tax model that can be used to simulate changes to federal tax policy to conduct revenue scoring, distributional impact, and, as seen in this paper, the implementation of a universal basic income. The model is continually being updated as contributions are made, so the results from the calculations seen in this paper may change as improvements are merged in.

\subsection{Data}
This paper utilizes two sets of data: the 2009 IRS Public Use File (PUF) and the 2014 Current Population Survey (CPS). The CPS was modified to include the imputed welfare benefit data used in Part A so we can assess the benefits paid out for specific programs.

Part A uses only the modified CPS data after it has undergone a procedure to create tax unit equivalents. At a high level, it is assumed that there is at least one tax unit per household in the CPS, and each household can be categorized in one of three ways: single persons living alone, individuals living in group quarters, and all other family structures.

In the first two structures, each individual is assumed to be one tax unit. For all other household types, the program iterates through each individual in the household, building a tax unit from the relationships implied by the data.

The code for the tax unit creation process is available on \href{https://github.com/open-source-economics/taxdata}{GitHub}.

After the CPS based tax units are created, a fully constrained, predictive mean matching process is performed between the CPS file and the PUF to create a final matched-PUF file. The matching procedure partitions the CPS and PUF files across several dimensions and matches the two files within each dimension to create fully representative tax units. The dataset is then extrapolated in three stages.

Stage one uses per capita adjustment factors derived from the CBO economic outlook to ensure the aggregated variables match macroeconomic growth rate projections. In stage two, a a linear programming algorithm is applied to adjust the weights on each record so that specified variables sum up to their targets. Stage three applies adjustment ratios to targeted variables to fine-tune their distribution so that it is consistent with that found in publicly available IRS data.

\pagebreak
\subsection{Welfare and Transfer Programs}
The following table shows the welfare and transfer programs programs were cut as part of the reforms. 

\singlespacing
\begin{table}[H]
\caption{Welfare Programs Cut}
\begin{center}
\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{lr}
\toprule
Program & Cost (million \$) \\
\midrule
Railroad retirement (excl. social security ) & 8,803 \\
Unemployment Assistance & 43,504 \\
Children's health insurance & 9,317 \\
Indian health & 4,510 \\
Health resources and services & 7,604 \\
Substance abuse and mental health services & 3,193 \\
Center for Medicare and Medicaid Innovation & 997 \\
Refundable Premium Tax Credit and Cost Sharing Reductions & 13,068 \\
Other & 12,834 \\
Student assistance--Department of Education and other & 56,337 \\
Housing assistance & 46,600 \\
Child nutrition and special milk programs & 19,490 \\
Supplemental feeding programs (WIC and CSFP) & 6,266 \\
Commodity donations and other & 823 \\
Family support payments to States and TANF & 20,378 \\
Low income home energy assistance & 3,537 \\
Payments to States for daycare assistance & 5,064 \\
Veterans non-service connected pensions & 5,251 \\
Payments to States--Foster Care/Adoption Assist. & 6,868 \\
Payment where child credit exceeds tax liability & 21,490 \\
Other public assistance & 1,071 \\
Coal miners and black lung benefits & 426 \\
Aging services programs & 1,462 \\
Energy employees compensation fund & 1,052 \\
September 11th victim compensation & 49 \\
Refugee assistance and other & 4,403 \\
Farm income stabilization (351) & 20,012 \\
Agricultural research and services (352) & 4,374 \\
Community development (451) & 7,896 \\
Area and regional development (452) & 3,027 \\
Disaster relief and insurance (453) & 9,747 \\
Social services (506) & 17,299 \\
Medicare & 505,053 \\
Medicaid & 401,201 \\
SSI & 56,068 \\
SNAP & 69,313 \\
Social Security & 749,467 \\
Veterans' Benefits & 134,672 \\
\bottomrule
\end{tabular}
\end{adjustbox}
\end{center}
%\floatfoot{Source: Literature and author's calculations.}
\end{table}
\doublespacing 

\subsection{Benefit Data Imputation}
Benefit and participation levels for welfare and transfer programs are consistently underreported in the Current Population Survey, making it difficult to get a true dollar figure for the cost of each program. To account for this, individual benefit levels for Supplemental Security Income (SSI), Supplemental Nutrition Assistance Program (SNAP), Veterans’ Benefits, Social Security, Medicare, and Medicaid were imputed using the open-source CPS Transfer Augmentation Model (C-TAM). C-TAM corrects for under-reported benefit use, imputes benefit payments where they are excluded, and imputes the marginal tax rate of these welfare and transfer programs. C-TAM can be found on \href{http://www.github.com/open-source-economics/benefits}{GitHub}.


\subsection{Welfare Multiples}

Welfare multiples were drawn from the literature when possible. Little work has been done on Veterans' Benefits, requiring the author to approximate the welfare cost. This was done by aggregating the welfare multiples from other government programs that provide similar services included in Veterans' Benefits. The Veteran's Benefits Association (VBA) Annual Benefits Reports provides a convenient basis for accomplishing this, dividing the benefits into size sections: compensation, pension and fiduciary, education, vocational rehabilitation and employment, insurance, and home loan guaranty. The amount spent on these programs in FY2014 is shown in the following table, along with the share of spending.\footnote{\href{http://www.benefits.va.gov/REPORTS/abr/ABR-IntroAppendix-FY14-11032015.pdf}{Veterans Benefits Administration. \textit{Annual Benefits Report: Fiscal Year 2014}.}}

\begin{table}[H]
\caption{Total Program Expenditures (2014)}
\begin{center}
\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{lrrr}
\toprule
Program 									&  Dollars (millions) 	& Percent of Total	&	Welfare Multiple 	\\
\midrule
Compensation 								&	64,356				& 74.55				&	0.99				\\		
Pension and Fiduciary 						&	5,462				& 6.33				&	0.95				\\
Education 									&	12,292				& 14.24				&	1.00				\\
Vocational Rehabilitation and Employment 	&	1,063				& 1.23				&	0.50				\\
Insurance									&	1,117				& 1.29				&	0.50				\\
Home Loan Guaranty 							& 	2,031				& 2.35				&	0.50				\\
Total 										& 	86,321				& 100.00			&	0.96				\\
\bottomrule
\end{tabular}
\end{adjustbox}
\end{center}
\floatfoot{Source: Drawn from literature and author's calculations.}
\end{table}

Compensation includes service-connected disability or death benefits. Pension and fiduciary includes veterans' non-service-connected pension and survivor's pension. Education includes all education benefit programs for veterans. Insurance includes the veterans' life insurance program. Home loan guaranty helps eligible veterans, active duty personnel, surviving spouses, and members of reserves and National Guard purchase, retain, and adapt homes. Vocational rehabilitation helps veterans who are unable to gain secure employment due to their service connected disabilities.

The vast majority of expenditures ($75.55\%$) are on compensation -- essentially transfer payments. These payments are exempt from tax and can be paid to the Veteran or their surviving beneficiary.\footnote{\href{http://www.benefits.va.gov/REPORTS/abr/ABR-Compensation-FY14-10202015.pdf}{Veterans Benefits Administration. "Annual Benefits Report: Compensation."}} These benefits are paid out in scales according to injury and disability, thus there could be a discrepancy between the prescribed amount and actual amount, causing a welfare loss. Because these are transfer payments, the welfare cost should be relatively small. Given SSI is assumed to have a welfare multiple of $0.99$, we use that for VB compensation as well.

Education benefits are the second largest segment of program expenditures ($14.24\%$). Angrist (1993) finds that use of Veterans' Benefits (specifically education benefits) raises annual earnings by $6\%$.\footnote{\href{http://www.jstor.org/stable/2524309}{Angrist, Joshua D. “The Effect of Veterans Benefits on Education and Earnings.” ILR Review. Vol. 46, No. 4 (Jul., 1993), pp. 637-652.}} $77\%$ of those that attend college or graduate school under Veterans' Benefits receive this premium. The author performs simple calculations with a discount of $10\%$ a year, finding that over one's working life the premium of a discounted 1986 dollar value was $17,717$ dollars. The author concludes that Veterans' Benefits do not appear to be socially wasteful.\footnote{Ibid.} This suggests the welfare multiple for education benefits is close to one, if not above one.

Pension and fiduciary are responsible for $6.33\%$ of spending. These programs provide similar benefits to the Social Security program, which has an approximated welfare multiple of $0.95$. We feel this is reasonable to apply to the pension and fiduciary part of Veterans' Benefits.

The remaining sections make up a relatively small portion of VA benefits expenditures ($.88\%$, total). If these programs are assumed to have a welfare multiple of zero, the weighted average welfare multiple across sections is $0.95\%$. If we assume at least a welfare multiple of $0.50$ for these programs -- that is at least $50$ cents for every dollar of spending -- then the welfare multiple rises to $0.97$. A conservative estimate would have the welfare multiple somewhere between $0.95$ and $0.97$, say $0.96$.

\begin{sidewaystable}
\caption{Welfare Multiples}
\centering
\label{Measures of In-kind Program Welfare Effects}
\begin{tabularx}{\textwidth}{l X l X}
\toprule
Program		&		
Author		&		
Years		&
Findings	\\
\midrule
% row 1
Social Security	&
Hong and Rios-Rull (2006)	&
$0.87755^1$, $0.87866^2$ &
$^1$Uses consumption equivalence compared to the steady-state;
$^2$Uses consumption born interpolation. \\

% row 2
Social Security	&
Peterman and Sommer (2014)		&
$0.925$ &
Measures ex ante welfare of expected lifetime consumption (CEV). \\

% row 3
Social Security	&
Feldstein (1974)		&
&
$11\%$ of GNP \\

% row 4
Social Security	&
Hubbard and Judd (2017)		&
$0.9625$, $0.9597$ &
Range depends on specification. \\ 

% row 5
Social Security	&
Storesletten, Telmer, and Yaron (1999)		&
$0.9625^4$, $0.9597^5$ &
$^4$Abolishing system; $^5$Privatizing $1/2$ system. \\

% row 6
Social Security	&
Auerbach and Kotlikoff (1987)		&
&
$6\%$ of full-time resources. \\

% row 7
Social Security	&
İmrohoroǧlu, İmrohoroǧlu, and Joines (1995)		&
&
$-2.08\%$ of GNP from removing Social Security. \\

% row 8
SNAP				&
Smeeding (1982)		&
$0.97$ 				&
\\

% row 9
SNAP				&
Moffitt (1989)		&
$1.00$ 				&
\\

% row 10
SNAP				&
Whitmore (2002)		&
$0.80$ 				&
\\

% row 11
Medicare			&
Lustig (2009)		&
$0.78$ 				&
For Medicare Part C. \\

% row 12
Medicare			&
Hall (2007)		&
$0.72$ 				&
For Medicare HMOs. \\

% row 13
Medicare			&
Finkelstein and McKnight (2008)		&
$0.45$, $0.75$ 				&
Range defends on specification. \\

% row 14
Medicaid			&
Finkelstein, Hendren, and Luttmer (2015)		&
$0.20$, $0.40$ 				&
Range defends on specification. \\

% row 15
Medicaid			&
Gallen (2015)		&
$0.24$, $0.35$ 				&
Range defends on specification. \\

% row 16
Medicaid			&
Liber and Lockenwood (2013)		&
$0.91$, $0.98$ 				&
For the Medicaid Home Care program. \\

% row 17
Housing				&
Desmond and Perkins (2016)		&
$0.90$				&
Uses HCV program in Milwaukee. \\

% row 18
Housing				&
Apgar (1990)		&
$0.87$				&
\\

% row 18
SSI				&
Peterman and Sommer (2014)		&
$0.988$				&
\\

\bottomrule
\end{tabularx}
\end{sidewaystable}

\end{document}
