

# clear

Clears the content of this string builder making it empty and returns this instance.

```kotlin
@IgnorableReturnValueexpect fun StringBuilder.clear(): StringBuilder(source)
```

```kotlin
fun main() {
    val sb = StringBuilder("Hello, Kotlin!")
    println("Before clear: '${sb.toString()}'") // prints: Hello, Kotlin!
    sb.clear()
    println("After clear: '${sb.toString()}'")   // prints: (empty string)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/clear.html)

    