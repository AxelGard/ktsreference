

# substringAfterLast

Returns a substring after the last occurrence of delimiter. If the string does not contain the delimiter, returns missingDelimiterValue which defaults to the original string.

```kotlin
fun String.substringAfterLast(delimiter: Char, missingDelimiterValue: String = this): String(source)
```

```kotlin
val path = "/home/user/docs/file.txt"

val fileName = path.substringAfterLast('/')
println(fileName)          // prints: file.txt

val plain = "filename".substringAfterLast('/', "no delimiter")
println(plain)             // prints: filename
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/substring-after-last.html)

    