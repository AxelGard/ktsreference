

# toPattern

Converts the string into a regular expression Pattern optionally with the specified flags from Pattern or'd together so that strings can be split or matched on.

```kotlin
inline fun String.toPattern(flags: Int = 0): Pattern(source)
```

```kotlin
import java.util.regex.Pattern

fun main() {
    // Simple pattern from a string
    val pattern = "a+b".toPattern()               // Pattern for regex "a+b"
    val text = "aaab"

    val matcher = pattern.matcher(text)
    println(matcher.matches())                    // prints: true

    // Pattern with a flag (case‑insensitive)
    val ciPattern = "hello".toPattern(Pattern.CASE_INSENSITIVE)
    val ciMatcher = ciPattern.matcher("HELLO")
    println(ciMatcher.find())                     // prints: true
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-pattern.html)

    