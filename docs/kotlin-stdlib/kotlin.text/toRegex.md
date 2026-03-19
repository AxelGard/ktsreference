

# toRegex

Converts the string into a regular expression Regex with the default options.

```kotlin
inline fun String.toRegex(): Regex(source)
```

```kotlin
fun main() {
    val regex = "\\d{4}".toRegex()          // 4-digit number pattern
    val text  = "The year 2024 is coming."

    val match = regex.find(text)
    println(match?.value)                    // prints: 2024
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-regex.html)

    