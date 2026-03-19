

# deleteCharAt

Warning since 1.4

```kotlin
inline fun StringBuilder.deleteCharAt(index: Int): StringBuilder(source)
```

```kotlin
fun main() {
    val sb = StringBuilder("Hello, world!")
    println("Before: $sb")
    sb.deleteCharAt(5)  // remove the comma
    println("After: $sb")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/delete-char-at.html)

    