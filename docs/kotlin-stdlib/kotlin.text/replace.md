

# replace

Replaces all occurrences of the given regular expression regex in this char sequence with the specified replacement expression.

```kotlin
inline fun CharSequence.replace(regex: Regex, replacement: String): String(source)
```

```kotlin
val input = "Hello 123 world 456"
val regex = "\\d+".toRegex()
val output = input.replace(regex, "#")
println(output)  // prints: Hello # world #
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/replace.html)

    