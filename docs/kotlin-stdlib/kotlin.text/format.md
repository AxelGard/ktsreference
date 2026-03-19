

# format

Uses this string as a format string and returns a string obtained by substituting format specifiers in the format string with the provided arguments, using the default locale.

```kotlin
inline fun String.format(vararg args: Any?): String(source)
```

```kotlin
fun main() {
    val firstName = "John"
    val age = 30
    val formatted = "Hello, %s! You are %d years old.".format(firstName, age)
    println(formatted)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/format.html)

    