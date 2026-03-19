

# split

Splits this char sequence to a list of strings around occurrences of the specified delimiters.

```kotlin
fun CharSequence.split(vararg delimiters: String, ignoreCase: Boolean = false, limit: Int = 0): List<String>(source)
```

fun main() {
    val sentence = "Kotlin,Java,Python"
    val languages = sentence.split(",")
    println(languages) // [Kotlin, Java, Python]
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/split.html)

    