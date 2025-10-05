#include<bits/extc++.h>
using namespace std;
mt19937 rng;
chrono::system_clock::time_point start, finish;
chrono::system_clock::duration elapsed = chrono::system_clock::duration::zero();
int test = 0, best = 0, score = 0, batch = 0, total = 0;
string TID, SID, LNG, comment, content, word;
int cpp = 1, java = 2, py = 2;
int timeLimit = cpp, nBatch = 10;
int tn6 = 1000000;
int weight[] = { 0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 4 };
int nTest[] = { 0, 1, 1, 2, 100000, 25000, 4000, 1000, 250, 40, 10 };
int maxN[] = { 0, 7, 14, 5, 10, 20, 50, 100, 200, 500, 1000 };
int maxAi[] = { 0, 10, 100, tn6, tn6, tn6, tn6, tn6, tn6, tn6, tn6 };
vector<string> OutputBi;
vector<int> InputN;
vector<vector<int>> InputA;
inline void exitBatch(string verdict) {
    if (ifstream(verdict + ".txt").peek() == ifstream::traits_type::eof()) {
        getline(ifstream("in.txt"), content, '\0');
        (ofstream(verdict + ".txt") << content).close();
    }
    cout << verdict << " on Batch " << batch << "\n", exit(1);
}
inline void assertThrow(bool condition) {
    if (!condition) throw exception();
}
inline int getRandInt(int low, int high) {
    return uniform_int_distribution<int>(low, high)(rng);
}
inline void prepareInput() {
    if (batch == 1) {
        InputA = { {4, 2, 4, 7, 1, 6, 1} };
    }
    else if (batch == 2) {
        InputA = { {4, 8, 2, 9, 1, 5, 4, 6, 8, 1, 7, 13, 11, 8} };
    }
    else if (batch == 3) {
        InputA = { {3, 5, 9, 7, 1}, {221} };
    }
    else {
        InputN.resize(nTest[batch]);
        InputA.resize(nTest[batch]);
        for (test = 0; test < nTest[batch]; ++test) {
            InputN[test] = getRandInt(1, maxN[batch]);
            InputA[test].resize(InputN[test]);
            for (int i = 0; i < InputN[test]; ++i)
                InputA[test][i] = getRandInt(1, maxAi[batch]);
        }
    }
    InputN.resize(nTest[batch] = InputA.size());
    for (test = 0; test < nTest[batch]; ++test)
        InputN[test] = InputA[test].size();
    ofstream fout("in.txt");
    for (fout << nTest[batch] << '\n', test = 0; test < nTest[batch]; ++test) {
        fout << InputN[test] << '\n' << InputA[test][0];
        for (int i = 1; i < InputN[test]; ++i) fout << " " << InputA[test][i];
        fout << '\n';
    }
    fout.close();
}
inline void validateOutput() {
    try {
        for (ifstream fin("out.txt"); fin >> word; OutputBi.push_back(word))
            stoi(word);
        assertThrow(OutputBi.size() ==
            accumulate(InputN.begin(), InputN.end(), 0));
        int k = 0;
        for (test = 0; test < nTest[batch]; ++test) {
            for (int j = 0, i = 0; i < InputN[test];) {
                for (j = i; j < InputN[test] &&
                    (InputA[test][j] ^ InputA[test][i] ^ 1) & 1; ++j);
                sort(InputA[test].begin() + i, InputA[test].begin() + j);
                for (; i < j; ++i)
                    assertThrow(InputA[test][i] == stoi(OutputBi[k++]));
            }
        }
    }
    catch (...) {
        exitBatch("WrongAnswer");
    }
}
inline void limitTime() {
    this_thread::sleep_for(chrono::seconds(timeLimit + 1));
    if (elapsed == chrono::system_clock::duration::zero())
        exitBatch("TimeLimitExceeded");
}
inline void updateSubmission() {
    system(("echo " + comment + to_string(score) + " " + SID +
        " %COMPUTERNAME% %USERNAME%>" + TID + "_" + SID + "." + LNG).c_str());
    getline(ifstream("Solution." + LNG), content, '\0');
    (ofstream(TID + "_" + SID + "." + LNG, ios::app) << content).close();
    cout << "Submission updated: " << TID + "_" + SID + "." + LNG << endl;
}
inline void printScoreAndExit() {
    cout << "Tentative score = " << double(score) / max(total, 1) << "/1\n";
    exit(0);
}
int main(int argc, char** argv) {
    TID = argv[1], SID = argv[2], LNG = argv[3];
    if (LNG == "cpp") timeLimit = cpp;
    else if (LNG == "java") timeLimit = java;
    if (LNG == "py") timeLimit = py, comment = "## ";
    else comment = "// ";
    if (argc == 5) {
        rng.seed(batch = stoi(argv[4]));
        cout << "Running on Batch " << batch << endl;
        prepareInput(), thread(limitTime).detach();
        start = chrono::high_resolution_clock::now();
        if ((LNG == "cpp" && system("b.exe<in.txt>out.txt")) ||
            (LNG == "java" && system("java Solution<in.txt>out.txt")) ||
            (LNG == "py" && system("pypy Solution.py<in.txt>out.txt")))
            exitBatch("RunTimeError");
        finish = chrono::high_resolution_clock::now();
        elapsed = chrono::duration_cast<chrono::nanoseconds>(finish - start);
        if (chrono::seconds(timeLimit) < elapsed)
            exitBatch("TimeLimitExceeded");
        validateOutput();
        cout << fixed << setprecision(9) << "Accepted on Batch " <<
            batch << " in " << (elapsed.count() * 1e-9) << "s\n", exit(0);
    }
    if (!ifstream(TID + "_" + SID + "." + LNG)) updateSubmission();
    getline(ifstream("Solution." + LNG), content, '\0');
    for (char& c : content) c = tolower(c);
    for (ifstream fin(TID + "_Forbidden.txt"); fin >> word;)
        if (content.find(word) != string::npos)
            cout << "ForbiddenKeyword: " << word << "\n", printScoreAndExit();
    if ((LNG == "cpp" && system("c++ Solution.cpp -o b.exe")) ||
        (LNG == "java" && system("javac Solution.java")) ||
        (LNG == "py" && system("pypy -m py_compile Solution.py")))
        cout << "CompilationError\n", printScoreAndExit();
    ofstream("RunTimeError.txt").close();
    ofstream("TimeLimitExceeded.txt").close();
    ofstream("WrongAnswer.txt").close();
    ifstream(TID + "_" + SID + "." + LNG).ignore(3) >> best;
    for (batch = 1; batch <= nBatch; total += weight[batch], ++batch)
        if (!system(("a.exe " + string(argv[1]) + " " + string(argv[2])
            + " " + string(argv[3]) + " " + to_string(batch)).c_str()))
            score += weight[batch];
    if (best <= score) updateSubmission();
    printScoreAndExit();
}