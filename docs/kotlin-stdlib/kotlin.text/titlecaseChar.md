

# titlecaseChar

Converts this character to title case using Unicode mapping rules of the invariant locale.

```kotlin
expect fun Char.titlecaseChar(): Char(source)
```

```kotlin
fun main() {
    val lower = 'a'
    val title = lower.titlecaseChar()
    println(title) // prints: A

    val greek = 'γ'
    println(greek.titlecaseChar()) // prints: Γ
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/titlecase-char.html)

    