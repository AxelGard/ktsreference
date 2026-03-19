

# deleteAt

Removes the character at the specified index from this string builder and returns this instance.

```kotlin
@IgnorableReturnValueexpect fun StringBuilder.deleteAt(index: Int): StringBuilder(source)
```

fun main() {
    val sb = StringBuilder("Hello World")
    sb.deleteAt(5)
    println(sb)  // Output: HelloWorld
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/delete-at.html)

    